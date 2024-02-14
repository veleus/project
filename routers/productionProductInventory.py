from fastapi import APIRouter
from operations.productionProductInventory import create_task, get_task, update_task, delete_task
from dto.model import ProductionProductInventory
from database import db 
router = APIRouter()

@router.get('/productionProductInventory/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductInventory/')
async def post_productgroups(data: ProductionProductInventory):
    return create_task(db, data)

@router.put('/productionProductInventory/')
async def put_productgroups(data: ProductionProductInventory, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductInventory/')
async def del_productgroups(id: int):
    return delete_task(db, id)

