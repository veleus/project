from fastapi import APIRouter
from dto.model import ProductionProductAssemblySteps
from operations.productionproductassemblysteps import create_task, get_task, delete_task, update_task
from database import db 

router = APIRouter()

@router.get('/productionProductAssemblySteps/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductAssemblySteps/')
async def post_productgroups(data: ProductionProductAssemblySteps):
    return create_task(db, data)

@router.put('/productionProductAssemblySteps/')
async def put_productgroups(data: ProductionProductAssemblySteps, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductAssemblySteps/')
async def del_productgroups(id: int):
    return delete_task(db, id)

