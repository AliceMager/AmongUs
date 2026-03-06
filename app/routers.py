from fastapi import APIRouter
from app.models.deployment import Deployment
router = APIRouter()

@router.post("/deployments", tags=["users"])
async def create_deployment(deployment: Deployment):
    ...