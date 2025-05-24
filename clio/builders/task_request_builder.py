# builders/task_calendar_document_builders.py
from datetime import datetime

from pydantic import BaseModel

from clio_client.openapi_client.models.task_create_request import TaskCreateRequest
from clio_client.openapi_client.models.task_create_request_data import (
    TaskCreateRequestData,
)
from clio_client.openapi_client.models.task_create_request_data_assignee import (
    TaskCreateRequestDataAssignee,
)
from clio_client.openapi_client.models.task_create_request_data_matter import (
    TaskCreateRequestDataMatter,
)
from clio_client.openapi_client.models.task_create_request_data_task_type import (
    TaskCreateRequestDataTaskType,
)


# Input model for creating/updating tasks
class TaskInputModel(BaseModel):
    name: str
    description: str
    due_at: datetime | None = None
    assignee_id: int | None = None
    matter_id: int | None = None
    task_type_id: int | None = None
    priority: str | None = None
    status: str | None = None
    notify_assignee: bool | None = None
    notify_completion: bool | None = None
    permission: str | None = None
    time_estimated: int | None = None
    statute_of_limitations: bool | None = None


def build_task_create_request(input: TaskInputModel) -> TaskCreateRequest:
    data_kwargs = input.model_dump(exclude_unset=True)

    if input.assignee_id:
        data_kwargs["assignee"] = TaskCreateRequestDataAssignee(id=input.assignee_id)
    if input.matter_id:
        data_kwargs["matter"] = TaskCreateRequestDataMatter(id=input.matter_id)
    if input.task_type_id:
        data_kwargs["task_type"] = TaskCreateRequestDataTaskType(id=input.task_type_id)

    return TaskCreateRequest(data=TaskCreateRequestData(**data_kwargs))

