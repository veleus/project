from fastapi import APIRouter
from operations.stagesToMaterial import create_task, update_task, delete_task, get_task
from database import db
from dto.model import StagesToMaterial
router = APIRouter()

@router.get('/stagesToMaterial/')
async def get_warehouse(id: int):
    return get_task(db, id)

@router.post('/stagesToMaterial/')
async def post_warehouse(data: StagesToMaterial):
    return create_task(db, data)

@router.put('/stagesToMaterial/')
async def put_warehouse(data: StagesToMaterial, id: int):
    return update_task(db, data, id)

@router.delete('/stagesToMaterial/')
async def del_warehouse(id: int):
    return delete_task(db, id)