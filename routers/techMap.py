

from fastapi import APIRouter
from operations.techMap import create_task, update_task, delete_task, get_task
from database import db
from dto.model import TechMap
router = APIRouter()

@router.get('/techMap/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/techMap/' )
async def post_products(data: TechMap):
    return create_task(db, data)

@router.put('/techMap/')
async def put_products(data: TechMap, id: int):
    return update_task(db, data, id)

@router.delete('/techMap/')
async def del_products(id: int):
    return delete_task(db, id)

