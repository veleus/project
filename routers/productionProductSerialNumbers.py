from fastapi import APIRouter
from operations.productionProductSerialNumbers import create_task, update_task, delete_task, get_task
from database import db
from dto.model import ProductionProductSerialNumbers
router = APIRouter()

@router.get('/productionProductSerialNumbers/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductSerialNumbers/')
async def post_productgroups(data : ProductionProductSerialNumbers):
    return create_task(db, data)

@router.put('/productionProductSerialNumbers/')
async def put_productgroups(data : ProductionProductSerialNumbers, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductSerialNumbers/')
async def del_productgroups(id: int):
    return delete_task(db,id)

