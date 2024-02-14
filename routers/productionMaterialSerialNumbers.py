from fastapi import APIRouter
from database import db 
from dto.model import ProductionMaterialSerialNumbers
from operations.productionmaterialserialnumbers import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionMaterialSerialNumbers/')
async def get_productgroups(id: int):
    return get_task(db, id)
@router.post('/productionMaterialSerialNumbers/')
async def post_productgroups(data: ProductionMaterialSerialNumbers):
    return create_task(db, data)

@router.put('/productionMaterialSerialNumbers/')
async def put_productgroups(data: ProductionMaterialSerialNumbers, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialSerialNumbers/')
async def del_productgroups(id: int):
    return delete_task(db, id)

