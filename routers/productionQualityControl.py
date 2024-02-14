from fastapi import APIRouter
from operations.productionQualityControl import create_task, update_task, delete_task, get_task
from database import db
from dto.model import ProductionQualityControl
router = APIRouter()

@router.get('/productionQualityControl/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionQualityControl/')
async def post_productgroups(data: ProductionQualityControl):
    return create_task(db, data)

@router.put('/productionQualityControl/')
async def put_productgroups(data: ProductionQualityControl, id: int):
    return update_task(db, data, id)

@router.delete('/productionQualityControl/')
async def del_productgroups(id: int):
    return delete_task(db, id)

