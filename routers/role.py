

from fastapi import APIRouter
from operations.role import create_task, get_task, update_task,delete_task
from database import db
from dto.model import Role
router = APIRouter()

@router.get('/role/')
async def get_products(id: int):
    return get_task(db,id)

@router.post('/role/')
async def post_products(data: Role):
    return create_task(db,data)

@router.put('/role/')
async def put_products(data: Role, id: int):
    return update_task(db,data,id)

@router.delete('/role/')
async def del_products(id: int):
    return delete_task(db, id)

