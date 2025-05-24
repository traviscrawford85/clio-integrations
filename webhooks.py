# webhooks.py
# FastAPI routes for handling Clio webhook events
from fastapi import APIRouter, Request

from clio.calculators import compute_limitations_date
from clio.matters import update_matter_limitations_date
from clio.validators import validate_matter_data

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
        # You need to specify the correct custom_field_id here
        custom_field_id = custom_fields.get("Limitations Date Field ID")
        update_matter_limitations_date(matter["id"], limitations_date, custom_field_id)
        return {"status": "success", "limitations_date": limitations_date}
    
    return {"status": "error", "message": "Could not compute limitations date"}
