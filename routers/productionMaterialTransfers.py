from fastapi import APIRouter
from dto.model import ProductionMaterialTransfers
from operations.productionproductexpiration import create_task, get_task, update_task, delete_task
from database import db 
router = APIRouter()

@router.get('/productionMaterialTransfers/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialTransfers/')
async def post_productgroups(data: ProductionMaterialTransfers):
    return create_task(db, data)

@router.put('/productionMaterialTransfers/')
async def put_productgroups(data: ProductionMaterialTransfers, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialTransfers/')
async def del_productgroups(id: int):
    return delete_task(db, id)

