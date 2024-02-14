from fastapi import APIRouter
from operations.productionWorkOrderStages import create_task, get_task, update_task, delete_task
from database import db
from dto.model import ProductionWorkOrderStages
router = APIRouter()

@router.get('/productionWorkOrderStatus/')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionWorkOrderStatus/')
async def post_productgroups(data : ProductionWorkOrderStages):
    return create_task(db,data)

@router.put('/productionWorkOrderStatus/')
async def put_productgroups(data: ProductionWorkOrderStages, id: int):
    return update_task(db,data,id)

@router.delete('/productionWorkOrderStatus/')
async def del_productgroups(id:int):
    return delete_task(db, id)

