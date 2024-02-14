from fastapi import APIRouter
from operations.productionWorkOrderStages import create_task, get_task, update_task, delete_task
from dto.model import ProductionWorkOrderStages
from database import db 
router = APIRouter()

@router.get('/productionWorkOrderStages/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionWorkOrderStages/')
async def post_productgroups(data: ProductionWorkOrderStages):
    return create_task(db, data)

@router.put('/productionWorkOrderStages/')
async def put_productgroups(data: ProductionWorkOrderStages, id):
    return update_task(db, data, id)

@router.delete('/productionWorkOrderStages/')
async def del_productgroups(id: int): 
    return delete_task(db,id)

