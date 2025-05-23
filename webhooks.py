# webhooks.py
# FastAPI routes for handling Clio webhook events
from fastapi import APIRouter, Request
from clio.validators import validate_matter_data
from clio.calculators import compute_limitations_date
from clio.matters import update_matter_limitations_date

router = APIRouter()

@router.post("/webhook/matter")
async def matter_webhook(request: Request):
    payload = await request.json()
    matter = payload.get("matter", {})
    
    errors = validate_matter_data(matter)
    if errors:
        return {"status": "validation_failed", "errors": errors}

    custom_fields = matter.get("custom_fields", {})
    incident_date = custom_fields.get("Date of Incident")
    limitations_date = compute_limitations_date(incident_date)

    if limitations_date:
        update_matter_limitations_date(matter["id"], limitations_date)
        return {"status": "success", "limitations_date": limitations_date}
    
    return {"status": "error", "message": "Could not compute limitations date"}
