from fastapi import APIRouter
from operations.productionmachinemaintenance import get_task, create_task, update_task, delete_task
from database import db
from dto.model import ProductionMachineMaintenance
router = APIRouter()

@router.get('/productionMachineMaintenance/')
async def get_productgroups(id : int):
    return get_task(db,id)

@router.post('/productionMachineMaintenance/')
async def post_productgroups(data : ProductionMachineMaintenance):
    return create_task(db,data)

@router.put('/productionMachineMaintenance/')
async def put_productgroups(data : ProductionMachineMaintenance, id : int):
    return update_task(db,data,id)

@router.delete('/productionMachineMaintenance/')
async def del_productgroups(id: int):
    return delete_task(db, id)

