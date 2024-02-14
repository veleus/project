

from fastapi import APIRouter
from operations.products import create_task, get_task, update_task, delete_task
from database import db
from dto.model import Products
router = APIRouter()

@router.get('/products/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/poducts/')
async def post_products(data: Products):
    return create_task(db,data)

@router.put('/products/')
async def put_products(data: Products, id: int):
    return update_task(db, data, id)

@router.delete('/products/')
async def del_products(id: int):
    return delete_task(db, id)

