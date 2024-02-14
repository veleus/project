from fastapi import APIRouter
from database import db
from operations.emploees import create_task, delete_task, update_task, get_task
from dto.model import Employee
router = APIRouter()

@router.get('/employees/')
async def get_employeess(id: int):
    return get_task(db, id)

@router.post('/employees/')
async def post_employees(data : Employee):
    return  create_task(db, data)

@router.put('/employees/')
async def put_employees(id, data : Employee):
    return update_task(db, id, data)

@router.delete('/employees/')
async def del_employees(id : int):
    return delete_task(db, id)
