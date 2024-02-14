from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialSurplus
from operations.productionьaterialsurplus import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionMaterialSurplus/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialSurplus/')
async def post_productgroups(data: ProductionMaterialSurplus):
    return create_task(db, data)

@router.put('/productionMaterialSurplus/')
async def put_productgroups(data: ProductionMaterialSurplus, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialSurplus/')
async def del_productgroups(id: int):
    return delete_task(db, id)

