

from fastapi import APIRouter
from operations.supplierOrderItems import create_task, get_task, update_task, delete_task
from database import db
from dto.model import SupplierOrderItems
router = APIRouter()

@router.get('/supplierOrderItems/')
async def get_products(id : int):
    return get_task(db, id)

@router.post('/supplierOrderItems/')
async def post_products(data: SupplierOrderItems):
    return create_task(db,data)

@router.put('/supplierOrderItems/')
async def put_products(data: SupplierOrderItems, id: int):
    return update_task(db, data, id)

@router.delete('/supplierOrderItems/')
async def del_products(id: int):
    return delete_task(db, id)

