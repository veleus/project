from fastapi import APIRouter
from dto.model import ProductionProductSales
from operations.productionProductSales import create_task, update_task, delete_task, get_task
from database import db 
router = APIRouter()

@router.get('/productionProductSales/')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionProductSales/')
async def post_productgroups(data : ProductionProductSales):
    return create_task(db,data)

@router.put('/productionProductSales/')
async def put_productgroups(data : ProductionProductSales, id: int):
    return update_task(db,data,id)

@router.delete('/productionProductSales/')
async def del_productgroups(id: int):
    return delete_task(db,id)

