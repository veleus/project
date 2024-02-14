from fastapi import APIRouter
from dto.model import ProductionProductReturnsReasons
from operations.productionproductReturnsReasons import create_task, get_task, delete_task, update_task
from database import db 
router = APIRouter()

@router.get('/productionProductReturnsReasons/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductReturnsReasons/')
async def post_productgroups(data: ProductionProductReturnsReasons):
    return create_task(db, data)

@router.put('/productionProductReturnsReasons/')
async def put_productgroups(data: ProductionProductReturnsReasons, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductReturnsReasons/')
async def del_productgroups(id: int):
    return delete_task(db, id)

