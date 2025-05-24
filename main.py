from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from clio.api.models.MatterViewModel import MatterViewModel
from clio.builders.matter_request_builder import MatterUpdateInputModel
from clio.services.matter_service import update_matter_custom_field
from clio.matters import get_matter_by_id
from clio_client.openapi_client.exceptions import UnauthorizedException
from clio.api.routes import clio_webhooks
from webhooks import router as webhooks_router
from clio_client.webhook_listener import router as webhook_listener_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your frontend domain(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhooks_router)  # For /webhook/matter
app.include_router(webhook_listener_router)  # For /webhook/matter_created


@app.get("/matters/{matter_id}", response_model=MatterViewModel)
def read_matter(matter_id: int):
    try:
        return get_matter_by_id(matter_id)  # 👈 Must return a structure matching MatterViewModel
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.patch("/matters/{matter_id}", response_model=MatterViewModel)
def update_matter(matter_id: int, payload: MatterUpdateInputModel):
    print("📦 Payload received:", payload)
    try:
        return update_matter_custom_field(matter_id, payload)
    except UnauthorizedException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Invalid or expired token."
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
