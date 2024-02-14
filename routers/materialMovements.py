

from fastapi import APIRouter
from database import db
from dto.model import MaterialMovements
from operations.materialsmovement import create_task, delete_task, update_task, get_task
router = APIRouter()

@router.get('/materialMovements/')
async def get_products(id: int):
    return get_task(db, id)

@router.post('/materialMovements/')
async def post_products(data : MaterialMovements):
    return create_task(db, data)

@router.put('/materialMovements/')
async def put_products(id, data : MaterialMovements):
    return update_task(db, data, id)

@router.delete('/materialMovements/')
async def del_products(id : int):
    return delete_task(db, id)

