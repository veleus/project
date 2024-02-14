from fastapi import APIRouter
from dto.model import Materials
from operations.materials import create_task, get_task, update_task, delete_task
from database import db 
router = APIRouter()

@router.get('/materials/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/materials/')
async def post_productgroups(data: Materials):
    return create_task(db, data)

@router.put('/materials/')
async def put_productgroups(data: Materials, id: int):
    return update_task(db, data, id)

@router.delete('/materials/')
async def del_productgroups(id: int):
    return delete_task(db, id)

