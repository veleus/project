from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialConsumption
from operations.productionmaterialconsumption import create_task, get_task, delete_task, update_task

router = APIRouter()

@router.get('/productionMaterialConsumption')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialConsumption')
async def post_productgroups(data: ProductionMaterialConsumption):
    return create_task(db, data)

@router.put('/productionMaterialConsumption/')
async def put_productgroups(data: ProductionMaterialConsumption, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialConsumption/')
async def del_productgroups(id: int):
    return delete_task(db, id)

