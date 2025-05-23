
import logging
from typing import List, Optional

import httpx
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class Matter(BaseModel):
    id: Optional[int]
    title: Optional[str]
    # Add more fields as needed

class Contact(BaseModel):
    id: Optional[int]
    name: Optional[str]
    # Add more fields as needed

class Task(BaseModel):
    id: Optional[int]
    description: Optional[str]
    # Add more fields as needed

class ClioApiClient:
    def __init__(self, token: str, base_url: str = "https://app.clio.com/api/v4", client: Optional[httpx.AsyncClient] = None):
        self.token = token
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }
        self.client = client or httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            timeout=httpx.Timeout(10.0, connect=5.0),
            follow_redirects=True
        )

    async def get_matters(self) -> List[Matter]:
        try:
            resp = await self.client.get("/matters")
            resp.raise_for_status()
            data = resp.json().get("data") or []
            return [Matter.model_validate(item) for item in data]
        except httpx.HTTPStatusError as e:
            logger.error(f"❌ Failed to fetch matters: {e.response.status_code} {e.response.text}")
            raise

    async def get_contacts(self) -> List[Contact]:
        try:
            resp = await self.client.get("/contacts")
            resp.raise_for_status()
            data = resp.json().get("data") or []
            return [Contact.model_validate(item) for item in data]
        except httpx.HTTPStatusError as e:
            logger.error(f"❌ Failed to fetch contacts: {e.response.status_code} {e.response.text}")
            raise

    async def get_tasks(self) -> List[Task]:
        try:
            resp = await self.client.get("/tasks")
            resp.raise_for_status()
            data = resp.json().get("data") or []
            return [Task.model_validate(item) for item in data]
        except httpx.HTTPStatusError as e:
            logger.error(f"❌ Failed to fetch tasks: {e.response.status_code} {e.response.text}")
            raise

    async def close(self):
        await self.client.aclose()


# Example usage for testing
if __name__ == "__main__":
    import asyncio

    async def main():
        token = "mock-token"  # Use .env or secure secrets in real apps
        client = ClioApiClient(token=token, base_url="http://localhost:8000")

        matters = await client.get_matters()
        for m in matters:
            print(f"Matter: {m}")

        contacts = await client.get_contacts()
        for c in contacts:
            print(f"Contact: {c}")

        tasks = await client.get_tasks()
        for t in tasks:
            print(f"Task: {t}")

        await client.close()

    asyncio.run(main())
