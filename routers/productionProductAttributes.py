from fastapi import APIRouter
from dto.model import ProductionProductAttributes
from database import db 
from operations.productionproductattributes import create_task, get_task, update_task, delete_task
router = APIRouter()

@router.get('/productionProductAttributes/')
async def get_productgroups(id:int):
    return get_task(db, id)

@router.post('/productionProductAttributes/')
async def post_productgroups(data: ProductionProductAttributes):
    return create_task(db, data)

@router.put('/productionProductAttributes/')
async def put_productgroups(data: ProductionProductAttributes , id:int):
    return update_task(db, data, id)

@router.delete('/productionProductAttributes/')
async def del_productgroups(id: int):
    return delete_task(db, id)

