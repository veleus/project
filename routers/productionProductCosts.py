from fastapi import APIRouter
from database import db 
from dto.model import ProductionProductCosts
from operations.productionproductcosts import get_task, create_task, update_task, delete_task
router = APIRouter()

@router.get('/productionProductCosts/')
async def get_productgroups(id):
    return get_task(id, db)

@router.post('/productionProductCosts/')
async def post_productgroups(data: ProductionProductCosts):
    return create_task(data, db)

@router.put('/productionProductCosts/')
async def put_productgroups(data: ProductionProductCosts, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductCosts/')
async def del_productgroups(id: int):
    return delete_task(db, id)


