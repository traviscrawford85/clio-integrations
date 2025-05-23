from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from services.statute_of_limitations_service import StatuteOfLimitationsService

router = APIRouter()
service = StatuteOfLimitationsService()

@router.post("/webhook/matter_created")
async def handle_matter_created(request: Request, background_tasks: BackgroundTasks):
    """
    Listener for Clio webhook on new Matter creation.
    """
    try:
        payload = await request.json()
        matter_id = payload.get("data", {}).get("id")
        date_of_incident = payload.get("data", {}).get("date_of_incident")

        if not matter_id:
            raise HTTPException(status_code=400, detail="Matter ID is missing in webhook payload.")

        background_tasks.add_task(process_statute_update, matter_id, date_of_incident)

        return {"status": "accepted", "matter_id": matter_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def process_statute_update(matter_id: int, date_of_incident: str):
    """
    Background task to compute and update statute of limitations.
    """
    statute_due_date = service.compute_statute_due_date(date_of_incident)
    if statute_due_date:
        payload = service.prepare_update_payload(status="pending", due_at=statute_due_date)
        # TODO: Perform API PATCH request to update matter in Clio system
        print(f"Would update Matter {matter_id} with statute date {statute_due_date}")
