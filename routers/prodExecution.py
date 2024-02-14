

from fastapi import APIRouter
from database import db
from dto.model import ProdExecution
from operations.prodexecution import create_task, update_task, delete_task, get_task
router = APIRouter()

@router.get('/prodExecution/')
async def get_products(id):
    return get_task(db, id)

@router.post('/prodExecution/')
async def post_products(data: ProdExecution):
    return create_task(db, data)

@router.put('/prodExecution/')
async def put_products(data: ProdExecution, id: int):
    return update_task(db, data, id)

@router.delete('/prodExecution/')
async def del_products(id: int):
    return delete_task(db, id)

