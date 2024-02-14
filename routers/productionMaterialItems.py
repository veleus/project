from fastapi import APIRouter
from operations.productionMaterialItems import create_task, get_task, update_task, delete_task
from dto.model import ProductionMaterialItems
from database import db 
router = APIRouter()

@router.get('/productionMaterialItems/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialItems/')
async def post_productgroups(data: ProductionMaterialItems):
    return create_task(db, data)

@router.put('/productionMaterialItems/')
async def put_productgroups(data: ProductionMaterialItems, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialItems/')
async def del_productgroupsid(id : int):
    return delete_task(db, id)

