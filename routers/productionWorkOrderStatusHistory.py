from fastapi import APIRouter
from operations.productionWorkOrderStatusHistory import create_task, delete_task, get_task, update_task
from database import db
from dto.model import ProductionWorkOrderStatusHistory
router = APIRouter()

@router.get('/productionWorkOrderStatusHistory/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionWorkOrderStatusHistory/')
async def post_productgroups(data: ProductionWorkOrderStatusHistory):
    return create_task(db, data)

@router.put('/productionWorkOrderStatusHistory/')
async def put_productgroups(data: ProductionWorkOrderStatusHistory, id: int):
    return update_task(db, data, id)
@router.delete('/productionWorkOrderStatusHistory/')
async def del_productgroups(id: int):
    return delete_task(db, id)

