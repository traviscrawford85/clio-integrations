# builders/task_builders.py
from datetime import datetime

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


def build_task_create_request(
    name: str,
    description: str,
    due_at: datetime | None = None,
    assignee_id: int | None = None,
    matter_id: int | None = None,
    task_type_id: int | None = None,
    priority: str | None = None,
    status: str | None = None,
    notify_assignee: bool | None = None,
    notify_completion: bool | None = None,
    permission: str | None = None,
    time_estimated: int | None = None,
    statute_of_limitations: bool | None = None
) -> TaskCreateRequest:

    data_kwargs = {
        "name": name,
        "description": description,
        "due_at": due_at,
        "priority": priority,
        "status": status,
        "notify_assignee": notify_assignee,
        "notify_completion": notify_completion,
        "permission": permission,
        "time_estimated": time_estimated,
        "statute_of_limitations": statute_of_limitations,
    }

    if assignee_id:
        data_kwargs["assignee"] = TaskCreateRequestDataAssignee(id=assignee_id, type="assignee")

    if matter_id:
        data_kwargs["matter"] = TaskCreateRequestDataMatter(id=matter_id)

    if task_type_id:
        data_kwargs["task_type"] = TaskCreateRequestDataTaskType(id=task_type_id)

    return TaskCreateRequest(data=TaskCreateRequestData(**data_kwargs))
