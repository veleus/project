from fastapi import APIRouter
from operations.productionWorkOrderItems import create_task, update_task, delete_task, get_task
from database import db
from dto.model import ProductionMaterialAttributes
router = APIRouter()

@router.get('/productionMaterialAttributes/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialAttributes/')
async def post_productgroups(data: ProductionMaterialAttributes):
    return create_task(db, data)

@router.put('/productionMaterialAttributes/')
async def put_productgroups(data: ProductionMaterialAttributes, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialAttributes/')
async def del_productgroups(id: int):
    return delete_task(db, id)