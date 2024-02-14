

from fastapi import APIRouter
from operations.supplierOrders import create_task, get_task, update_task, delete_task
from database import db
from dto.model import SupplierOrders
router = APIRouter()

@router.get('/supplierOrders/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/supplierOrders/')
async def post_products(data:SupplierOrders):
    return create_task(db, data)

@router.put('/supplierOrders/')
async def put_products(data:SupplierOrders, id: int):
    return update_task(db, data, id)

@router.delete('/supplierOrders/')
async def del_products(id: int):
    return delete_task(db, id)

