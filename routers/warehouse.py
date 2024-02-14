from fastapi import APIRouter
from operations.warehouse import create_task, get_task, update_task, delete_task
from database import db
from dto.model import Warehouse
router = APIRouter()

@router.get('/warehouse/')
async def get_warehouse(id: int):
    return get_task(db, id)

@router.post('/warehouse/')
async def post_warehouse(data: Warehouse):
    return  create_task(db, data)

@router.put('/warehouse/')
async def put_warehouse(data: Warehouse, id: int):
    return update_task(db, data, id)

@router.delete('/warehouse/')
async def del_warehouse(id: int):
    return delete_task(db, id)
