from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialDefects
from operations.productionmaterialdefects import create_task, update_task, delete_task, get_task 
router = APIRouter()

@router.get('/productionMaterialDefects/')
async def get_employees(id: int):
    return get_task(db, id)

@router.post('/productionMaterialDefects/')
async def post_employees(data: ProductionMaterialDefects):
    return create_task(db, data)

@router.put('/productionMaterialDefects/')
async def put_employees(data: ProductionMaterialDefects, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialDefects/')
async def del_employees(id: int):
    return delete_task(db,id)
