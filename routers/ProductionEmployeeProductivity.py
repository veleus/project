from fastapi import APIRouter
from database import db
from dto.model import ProductionEmployeeProductivity
from operations.productionemployeeproductivity import get_task, create_task, update_task, delete_task
router = APIRouter()

@router.get('/ProductionEmployeeProductivity/')
async def get_productgroups(id : int):
    return get_task(id)

@router.post('/ProductionEmployeeProductivity/')
async def post_productgroups(data : ProductionEmployeeProductivity):
    return create_task(db, data)

@router.put('/ProductionEmployeeProductivity/')
async def put_productgroups(data : ProductionEmployeeProductivity, id : int):
    return update_task(db, data, id)

@router.delete('/ProductionEmployeeProductivity/')
async def del_productgroups(id : int):
    return delete_task(db, id)

