from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialReturnsReasons
from operations.productionmaterialreturnsreasons import get_task, create_task, update_task, delete_task
router = APIRouter()

@router.get('/productionMaterialReturnsReasons/')
async def get_productgroups(id : int):
    return get_task(db,id)

@router.post('/productionMaterialReturnsReasons/')
async def post_productgroups(data : ProductionMaterialReturnsReasons):
    return create_task(db, data)

@router.put('/productionMaterialReturnsReasons/')
async def put_productgroups(data : ProductionMaterialReturnsReasons, id : int):
    return update_task(db, data, id)

@router.delete('/productionMaterialReturnsReasons/')
async def del_productgroups(id: int):
    return delete_task(db,id)

