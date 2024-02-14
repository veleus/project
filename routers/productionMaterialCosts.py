from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialCosts
from operations.productionmaterialconsumption import get_task, create_task, update_task, delete_task
router = APIRouter()

@router.get('/productionMaterialCosts/')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionMaterialCosts/')
async def post_productgroups(data: ProductionMaterialCosts):
    return create_task(db, data)

@router.put('/productionMaterialCosts/')
async def put_productgroups(data: ProductionMaterialCosts, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialCosts/')
async def del_productgroups(id: int):
    return delete_task(db, id)

