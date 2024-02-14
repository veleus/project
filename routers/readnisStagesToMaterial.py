

from fastapi import APIRouter
from operations.readnisStagesToMaterial import get_task, create_task, update_task, delete_task
from database import db
from dto.model import ReadnisStagesToMaterial
router = APIRouter()

@router.get('/readnisStagesToMaterial/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/readnisStagesToMaterial/')
async def post_products(data: ReadnisStagesToMaterial):
    return create_task(db, data)

@router.put('/readnisStagesToMaterial/')
async def put_products(data: ReadnisStagesToMaterial, id: int):
    return update_task(db, data, id)

@router.delete('/readnisStagesToMaterial/')
async def del_products(id: int):
    return delete_task(db,id)

