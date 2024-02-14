from fastapi import APIRouter
from database import db
from dto.model import ProductionEmployeeAttendance
from operations.productionemployeeattendance import get_task, update_task, deleate_task, create_task
router = APIRouter()

@router.get('/productionEmployeeAttendance/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionEmployeeAttendance/')
async def post_productgroups(data : ProductionEmployeeAttendance):
    return create_task(db, data)

@router.put('/productionEmployeeAttendance/')
async def put_productgroups(data: ProductionEmployeeAttendance, id: int):
    return update_task(db, data, id)

@router.delete('/productionEmployeeAttendance/')
async def del_productgroups(id: int):
    return deleate_task(db,id)

