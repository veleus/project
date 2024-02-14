from fastapi import APIRouter
from database import db 
from dto.model import ProductionMaterialRequestItems
from operations.productionmaterialrequestItems import get_task, update_task, delete_task, create_task
router = APIRouter()

@router.get('/productionMaterialRequestItems')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionMaterialRequestItems')
async def post_productgroups(data : ProductionMaterialRequestItems):
    return create_task(db,data)

@router.put('/productionMaterialRequestItems/')
async def put_productgroups(data : ProductionMaterialRequestItems, id: int):
    return update_task(db,data,id)

@router.delete('/productionMaterialRequestItems/')
async def del_productgroups(id : int):
    return delete_task(db, id)

