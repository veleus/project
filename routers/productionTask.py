

from fastapi import APIRouter
from operations.productionTask import create_task, delete_task, update_task, get_task
from database import db
from dto.model import ProductionTask
router = APIRouter()

@router.get('/productionTask/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/productionTask/')
async def post_products(data: ProductionTask):
    return create_task(db, data)

@router.put('/productionTask/')
async def put_products(data: ProductionTask, id: int):
    return update_task(db, data, id)

@router.delete('/productionTask/')
async def del_products(id: int):
    return delete_task(db, id)
