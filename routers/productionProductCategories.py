from fastapi import APIRouter
from database import db
from dto.model import ProductionProductCategories
from operations.productionproductcategories import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionProductCategories/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductCategories/')
async def post_productgroups(data: ProductionProductCategories):
    return create_task(db, data)

@router.put('/productionProductCategories/')
async def put_productgroups(data: ProductionProductCategories, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductCategories/')
async def del_productgroups(id: int):
    return delete_task(db, id)

