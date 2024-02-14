from fastapi import APIRouter
from operations.productionWorkOrders import create_task, get_task, update_task, delete_task
from database import db
from dto.model import ProductionWorkOrders
router = APIRouter()

@router.get('/productionWorkOrders/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionWorkOrders/')
async def post_productgroups(data: ProductionWorkOrders, id: int):
    return create_task(db, data, id)


@router.put('/productionWorkOrders/')
async def put_productgroups(data: ProductionWorkOrders, id: int):
    return update_task(db, data, id)

@router.delete('/productionWorkOrders/')
async def del_productgroups(id : int):
    return delete_task(db, id)

