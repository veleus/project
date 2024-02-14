

from fastapi import APIRouter
from operations.readnisStagesToProduct import create_task, get_task, update_task,delete_task
from database import db
from dto.model import ReadnisStagesToProduct
router = APIRouter()

@router.get('/readnisStagesToProduct/')
async def get_products(id: int):
    return get_task(db,id)

@router.post('/readnisStagesToProduct/')
async def post_products(data: ReadnisStagesToProduct, id):
    return create_task(db,data,id)

@router.put('/readnisStagesToProduct/')
async def put_products(data: ReadnisStagesToProduct, id: int):
    return update_task(db,data,id)

@router.delete('/readnisStagesToProduct/')
async def del_products(id: int):
    return delete_task(db, id)

