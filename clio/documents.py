from clio.token_store import get_access_token
from clio_client.openapi_client import ApiClient, Configuration
from clio_client.openapi_client.api.documents_api import DocumentsApi
from clio_client.openapi_client.models.document_update_request import (
    DocumentUpdateRequest,
)
from clio_client.openapi_client.models.document_update_request_data import (
    DocumentUpdateRequestData,
)


def _get_api() -> DocumentsApi:
    config = Configuration()
    config.api_key["Authorization"] = token  # just the token, no "Bearer"
config.api_key_prefix["Authorization"] = "Bearer"
    return DocumentsApi(ApiClient(config))


def list_documents(matter_id: int = None):
    return _get_api().document_index(matter_id=matter_id).to_dict()


def get_document(document_id: int):
    return _get_api().document_show(id=document_id).to_dict()


def update_document(document_id: int, title: str):
    payload = DocumentUpdateRequest(
        data=DocumentUpdateRequestData(title=title)
    )
    return _get_api().document_update(id=document_id, document_update_request=payload).to_dict()


def upload_document(file_path: str, title: str, matter_id: int):
    api = _get_api()
    with open(file_path, "rb") as file_data:
        return api.document_create_multipart(
            title=title,
            file=file_data,
            matter_id=matter_id
        ).to_dict()
