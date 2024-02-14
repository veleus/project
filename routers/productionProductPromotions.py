from fastapi import APIRouter
from operations.productionProductPromotions import create_task, get_task, update_task, delete_task
from dto.model import ProductionProductPromotions
from database import db 
router = APIRouter()

@router.get('/productionProductPromotions/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductPromotions/')
async def post_productgroups(data: ProductionProductPromotions):
    return create_task(db, data)

@router.put('/productionProductPromotions/')
async def put_productgroups(data: ProductionProductPromotions, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductPromotions/')
async def del_productgroupsid(id : int):
    return delete_task(db, id)

