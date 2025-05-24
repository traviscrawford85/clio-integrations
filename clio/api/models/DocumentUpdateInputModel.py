
from pydantic import BaseModel


class DocumentUpdateInputModel(BaseModel):
    title: str | None = None
    category_id: int | None = None
    is_shared: bool | None = None
    description: str | None = None
