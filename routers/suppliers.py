
from fastapi import APIRouter
from operations.suppliers import create_task, get_task, update_task, delete_task
from database import db
from dto.model import Suppliers
router = APIRouter()

@router.get('/suppliers/')
async def get_suppliers(id: int):
    return get_task(db, id)

@router.post('/suppliers/')
async def post_suppliers(data : Suppliers):
    return create_task(db, data)

@router.put('/suppliers/')
async def put_suppliers(data : Suppliers, id: int):
    return update_task(db, data, id)

@router.delete('/suppliers/')
async def del_suppliers(id: int):
    return delete_task(db, id)
