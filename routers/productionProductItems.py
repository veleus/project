

from fastapi import APIRouter
from operations.productionProductItems import create_task, get_task, update_task, delete_task
from database import db 
from dto.model import ProductionProductItems
router = APIRouter()

@router.get('/productionProductItems/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/productionProductItems/')
async def post_products(data: ProductionProductItems):
    return create_task(db, data)

@router.put('/productionProductItems/')
async def put_products(data: ProductionProductItems, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductItems/')
async def del_products(id: int):
    return delete_task(db, id)

