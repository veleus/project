from fastapi import APIRouter
from database import db
from dto.model import ProductionProductDefects
from operations.productionproductdefects import create_task, get_task, delete_task, update_task
router = APIRouter()

@router.get('/productionProductDefects/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductDefects/')
async def post_productgroups(data: ProductionProductDefects):
    return create_task(db, data)

@router.put('/productionProductDefects/')
async def put_productgroups(data: ProductionProductDefects, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductDefects/')
async def del_productgroups(id: int):
    return delete_task(db, id)

