from fastapi import APIRouter
from database import db 
from operations.productionmaterialforecast import get_task, update_task, create_task, delete_task
from dto.model import ProductionMaterialForecast
router = APIRouter()

@router.get('/productionMaterialForecast/')
async def get_productgroups(id : int):
    return get_task(db,id)

@router.post('/productionMaterialForecast/')
async def post_productgroups(data : ProductionMaterialForecast):
    return create_task(db,data)

@router.put('/productionMaterialForecast/')
async def put_productgroups(data : ProductionMaterialForecast, id : int):
    return update_task(db,data,id)

@router.delete('/productionMaterialForecast/')
async def del_productgroups(id: int):
    return delete_task(db,id)
