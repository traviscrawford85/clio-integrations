from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from clio.matters import update_matter_limitations_date

router = APIRouter()

@router.post("/webhook/matter_created")
async def matter_created_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    matter_id = payload.get("data", {}).get("id")
    # Compute limitations_date and custom_field_id as needed
    limitations_date = "2025-05-23"  # Example, replace with your logic
    custom_field_id = 12345          # Replace with your actual custom field ID

    if matter_id and limitations_date and custom_field_id:
        background_tasks.add_task(
            update_matter_limitations_date,
            matter_id=matter_id,
            limitations_date=limitations_date,
            custom_field_id=custom_field_id
        )
        return {"status": "scheduled"}
    else:
        raise HTTPException(status_code=400, detail="Missing required data")
