from fastapi import APIRouter, HTTPException, Request
from typing import Any
from app.services.api import APIService

router = APIRouter(prefix="/apis", tags=["APIs"])

@router.post("/")
async def create_api(request: Request):
    data = await request.json() 
    row = await APIService.create_api(data)
    return row 

@router.get("/{api_id}")
async def get_api(api_id: int):
    row = await APIService.get_api(api_id)
    if not row:
        raise HTTPException(404, "API not found")
    return row

@router.get("/")
async def list_apis():
    rows = await APIService.list_apis()
    return rows

@router.put("/{api_id}")
async def update_api(api_id: int, request: Request):
    data = await request.json()
    row = await APIService.update_api(api_id, data)
    if not row:
        raise HTTPException(404, "API not found or no fields updated")
    return row

@router.delete("/{api_id}")
async def delete_api(api_id: int):
    success = await APIService.delete_api(api_id)
    if not success:
        raise HTTPException(404, "API not found")
    return {"detail": "API deleted successfully"}

@router.get("/issues")
async def list_apis_with_issues():
    rows = await APIService.list_apis_with_issues()
    return rows
