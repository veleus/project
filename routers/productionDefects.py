from fastapi import APIRouter
from operations.productionsdefect import create_task, update_task, delete_task, get_task
from database import db
from dto.model import ProductionDefects
router = APIRouter()

@router.get('/productionDefects/', )
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionDefects/')
async def post_productgroups(data: ProductionDefects):
    return create_task(db, data)

@router.put('/productionDefects/')
async def put_productgroups(id: int, data: ProductionDefects):
    return update_task(db, data, id)

@router.delete('/productionDefects/')
async def del_productgroups(id: int):
    return delete_task(id)

