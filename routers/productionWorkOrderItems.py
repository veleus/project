from fastapi import APIRouter
from operations.productionWorkOrderItems import create_task, update_task, delete_task, get_task
from database import db
from dto.model import ProductionWorkOrderItems
router = APIRouter()

@router.get('/productionWorkOrderItems/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionWorkOrderItems/')
async def post_productgroups(data: ProductionWorkOrderItems):
    return create_task(db, data)

@router.put('/productionWorkOrderItems/')
async def put_productgroups(data: ProductionWorkOrderItems, id: int):
    return update_task(db, data, id)

@router.delete('/productionWorkOrderItems/')
async def del_productgroups(id: int):
    return delete_task(db, id)