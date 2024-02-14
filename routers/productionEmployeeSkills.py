from fastapi import APIRouter
from operations.productionemployeeskills import get_task, create_task, delete_task, update_task
from database import db
from dto.model import ProductionEmployeeSkills
router = APIRouter()

@router.get('/productionEmployeeSkills/')
async def get_productgroups(id : int):
    return get_task(db, id)

@router.post('/productionEmployeeSkills/')
async def post_productgroups(data : ProductionEmployeeSkills):
    return create_task(db, data)

@router.put('/productionEmployeeSkills/')
async def put_productgroups(data : ProductionEmployeeSkills, id : int):
    return update_task(db,data, id)

@router.delete('/productionEmployeeSkills/')
async def del_productgroups(id : int):
    return delete_task(db, id)

