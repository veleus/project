from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialCategories
from operations.productionmaterialcategories import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionMaterialCategories/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialCategories/')
async def post_productgroups(data: ProductionMaterialCategories):
    return create_task(db, data)

@router.put('/productionMaterialCategories/')
async def put_productgroups(id: int, data: ProductionMaterialCategories):
    return update_task(db, data, id)

@router.delete('/productionMaterialCategories/')
async def del_productgroups(id: int):
    return delete_task(db,id)

