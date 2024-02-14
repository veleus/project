

from fastapi import APIRouter
from operations.stages import create_task, get_task, update_task, delete_task
from database import db
from dto.model import Stages
router = APIRouter()

@router.get('/stages/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/stages/')
async def post_products(data: Stages):
    return create_task(db, data)

@router.put('/stages/')
async def put_products(data: Stages, id: int):
    return update_task(db, data, id)

@router.delete('/stages/')
async def del_products(id: int):
    return delete_task(db, id)

