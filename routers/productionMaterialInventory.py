from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialInventory
from operations.productionmaterialinventory import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionMaterialInventory/')
async def get_productgroups(id:int):
    return get_task(db,id)

@router.post('/productionMaterialInventory/')
async def post_productgroups(data:ProductionMaterialInventory):
    return create_task(db,data)

@router.put('/productionMaterialInventory/')
async def put_productgroups(data:ProductionMaterialInventory, id:int):
    return update_task(db,data, id)

@router.delete('/productionMaterialInventory/')
async def del_productgroups(id : int):
    return delete_task(db, id)

