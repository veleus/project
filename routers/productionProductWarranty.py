from fastapi import APIRouter
from operations.productionProductWarranty import create_task, update_task, delete_task, get_task
from database import db
from dto.model import ProductionProductWarranty
router = APIRouter()

@router.get('/productionProductWarranty/')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionProductWarranty/')
async def post_productgroups(data: ProductionProductWarranty):
    return create_task(db,data)

@router.put('/productionProductWarranty/')
async def put_productgroups(data: ProductionProductWarranty, id: int):
    return update_task(db,data,id)

@router.delete('/productionProductWarranty/')
async def del_productgroups(id: int):
    return delete_task(db,id)

