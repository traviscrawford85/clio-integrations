

from clio.services.webhooks import register_clio_webhook
from clio.token_store import get_access_token

register_clio_webhook(
    callback_url="https://7b3d-69-255-203-57.ngrok-free.app/webhooks/clio",
    event_types=["matter.create", "matter.update"],
    access_token=get_access_token()
)
