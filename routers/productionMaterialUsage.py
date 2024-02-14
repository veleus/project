from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialUsage
from operations.productionmaterialusage import get_task, update_task, delete_task, create_task
router = APIRouter()

@router.get('/productionMaterialUsage/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialUsage/')
async def post_productgroups(data: ProductionMaterialUsage):
    return create_task(db, data)

@router.put('/productionMaterialUsage/')
async def put_productgroups(data: ProductionMaterialUsage, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialUsage/')
async def del_productgroups(id: int):
    return delete_task(db, id)

