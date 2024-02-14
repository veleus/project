from fastapi import APIRouter
from operations.machines import create_task, update_task, delete_task, get_task
from database import db
from dto.model import Machines
router = APIRouter()

@router.get('/machines/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/machines/')
async def post_productgroups(data: Machines):
    return create_task(db, data)

@router.put('/machines/')
async def put_productgroups(data: Machines, id: int):
    return update_task(db, data, id)

@router.delete('/machines/')
async def del_productgroups(id: int):
    return delete_task(db, id)