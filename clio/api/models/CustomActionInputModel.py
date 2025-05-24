
from pydantic import BaseModel


class CustomActionUpdateInputModel(BaseModel):
    label: str | None = None
    target_url: str | None = None
    ui_reference: str | None = None
