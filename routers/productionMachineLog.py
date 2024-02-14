from fastapi import APIRouter
from operations.productionmachinelog import create_task, update_task, delete_task, get_task
from database import db
from dto.model import ProductionMachineLog
router = APIRouter()

@router.get('/productionMachineLog/')
async def get_productgroups(id : int):
    return get_task(db, id)

@router.post('/productionMachineLog/')
async def post_productgroups(data : ProductionMachineLog):
    return create_task(db, data)

@router.put('/productionMachineLog/')
async def put_productgroups(data : ProductionMachineLog, id : int):
    return update_task(db, data, id)

@router.delete('/productionMachineLog/')
async def del_productgroups(id : int):
    return delete_task(db, id)

