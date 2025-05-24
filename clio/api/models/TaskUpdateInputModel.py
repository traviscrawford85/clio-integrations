from datetime import date

from pydantic import BaseModel


class TaskUpdateInputModel(BaseModel):
    description: str | None = None
    due_at: date | None = None
    status: str | None = None
    priority: str | None = None
    assignee_id: int | None = None
    name: str | None = None
    matter_id: int | None = None
    task_type_id: int | None = None
    custom_field_values: list[dict] | None = None
    group_id: int | None = None
