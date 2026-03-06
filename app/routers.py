import datetime
import uuid
from fastapi import APIRouter
from app.models.deployment import Deployment
from app.db.postgres import Session
from app.tables.deployments import Deployments, Status
from app.validator import validate_deployment
router = APIRouter()

@router.post("/deployments", tags=["users"])
async def create_deployment(deployment: Deployment):
    validate_deployment(deployment)
    session = Session()
    dep_id = uuid.uuid4()
    new_deployment = Deployments(id=dep_id,db_name=deployment.db_name,
                    status=Status.CREATED,username=deployment.username, creation_time=datetime.datetime.now())
    session.add(new_deployment)
    session.commit()
    session.close()
    return dep_id