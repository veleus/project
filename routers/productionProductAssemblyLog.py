from fastapi import APIRouter
from database import db
from dto.model import ProductionProductAssemblyLog
from operations.productionproductassemblylog import create_task, get_task, delete_task, update_task, update_task
router = APIRouter()

@router.get('/productionProductAssemblyLog')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductAssemblyLog')
async def post_productgroups(data: ProductionProductAssemblyLog):
    return create_task(db, data)

@router.put('/productionProductAssemblyLog/')
async def put_productgroups(data: ProductionProductAssemblyLog, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductAssemblyLog/')
async def del_productgroups(id: int):
    return delete_task(db, id)

