from fastapi import APIRouter
from operations.productionProductReturns import create_task, get_task, update_task, delete_task
from database import db 
from dto.model import ProductionProductReturns
router = APIRouter()

@router.get('/productionProductReturns/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductReturns')
async def post_productgroups(data : ProductionProductReturns):
    return create_task(db, data)

@router.put('/productionProductReturns/')
async def put_productgroups(data : ProductionProductReturns, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductReturns/')
async def del_productgroups(id: int):
    return delete_task(db, id)

