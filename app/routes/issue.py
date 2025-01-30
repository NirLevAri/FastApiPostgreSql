from fastapi import APIRouter, HTTPException
from app.services.issue import IssueService

router = APIRouter(prefix="/issues", tags=["Issues"])

@router.post("/")
async def create_issue():
    row = await IssueService.create_issue()
    return row  

@router.get("/{issue_id}")
async def get_issue(issue_id: int):
    row = await IssueService.get_issue(issue_id)
    if not row:
        raise HTTPException(404, "Issue not found")
    return row

@router.get("/")
async def list_issues():
    return await IssueService.list_issues()

@router.delete("/{issue_id}")
async def delete_issue(issue_id: int):
    success = await IssueService.delete_issue(issue_id)
    if not success:
        raise HTTPException(404, "Issue not found")
    return {"detail": "Issue deleted"}
