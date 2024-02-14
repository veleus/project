from fastapi import APIRouter
from database import db 
from dto.model import ProductionMaterialRequests
from operations.productionmaterialrequests import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionMaterialRequests/')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionMaterialRequests/')
async def post_productgroups(data: ProductionMaterialRequests):
    return create_task(db,data)

@router.put('/productionMaterialRequests/')
async def put_productgroups(data: ProductionMaterialRequests, id: int):
    return update_task(db,data,id)

@router.delete('/productionMaterialRequests/')
async def del_productgroups(id: int):
    return delete_task(db, id)
