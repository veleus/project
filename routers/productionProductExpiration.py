from fastapi import APIRouter
from dto.model import ProductionProductExpiration
from operations.productionproductexpiration import create_task, get_task, update_task, delete_task
from database import db 
router = APIRouter()

@router.get('/productionProductExpiration/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductExpiration/')
async def post_productgroups(data: ProductionProductExpiration):
    return create_task(db, data)

@router.put('/productionProductExpiration/')
async def put_productgroups(data: ProductionProductExpiration, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductExpiration/')
async def del_productgroups(id: int):
    return delete_task(db, id)

