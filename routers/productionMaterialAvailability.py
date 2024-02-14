from fastapi import APIRouter
from operations.productionmaterialavailability import get_task, create_task, update_task, delete_task
from database import db
from dto.model import ProductionMaterialAvailability
router = APIRouter()

@router.get('/productionMaterialAvailability/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialAvailability/')
async def post_productgroups(data: ProductionMaterialAvailability):
    return create_task(db, data)

@router.put('/productionMaterialAvailability/')
async def put_productgroups(data: ProductionMaterialAvailability, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialAvailability/')
async def del_productgroups(id: int):
    return delete_task(db, id)

