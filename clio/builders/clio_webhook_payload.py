# Input model for Clio webhook payloads

from pydantic import BaseModel


class ClioWebhookPayload(BaseModel):
    event: str
    resource_type: str
    resource_id: int
    payload: dict | None = None