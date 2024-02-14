

from fastapi import APIRouter
from database import db

from operations.matertialmovmentitems import get_task, create_task, delete_task, update_task
from dto.model import MaterialMovementItems
router = APIRouter()

@router.get('/materialMovementItems/')
async def get_products(id: int):
    return get_task(db,id)

@router.post('/materialMovementItems/')
async def post_products(data : MaterialMovementItems):
    return create_task(db,data)

@router.put('/materialMovementItems/')
async def put_products(data : MaterialMovementItems, id: int):
    return update_task(db,data,id)

@router.delete('/materialMovementItems/')
async def del_products(id : int):
    return delete_task(db, id)

