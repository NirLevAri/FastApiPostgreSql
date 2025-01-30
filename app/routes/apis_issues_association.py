from fastapi import APIRouter, HTTPException
from app.services.apis_issues_association import AssociationService

router = APIRouter(prefix="/associations", tags=["API-Issue Associations"])

@router.post("/")
async def add_association(api_id: int, issue_id: int):
    success = await AssociationService.add_association(api_id, issue_id)
    if not success:
        return {"detail": "Api issues association already exists or insertion failed"}
    return {"detail": "Api issues association created"}

@router.delete("/")
async def remove_association(api_id: int, issue_id: int):
    success = await AssociationService.remove_association(api_id, issue_id)
    if not success:
        raise HTTPException(404, "No such api issues association found")
    return {"detail": "Api issues association removed"}
