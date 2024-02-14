from fastapi import APIRouter
from database import db 
from dto.model import ProductionProductComplaints
from operations.productionproductcomplaints import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionProductComplaints/')
async def get_productgroups(id: int):
    return get_task(id, db)

@router.post('/productionProductComplaints/')
async def post_productgroups(data: ProductionProductComplaints):
    return create_task(data, db)

@router.put('/productionProductComplaints/')
async def put_productgroups(data: ProductionProductComplaints, id: int):
    return update_task(data, db, id)

@router.delete('/productionProductComplaints/')
async def del_productgroups(db,id: int):
    return delete_task(db,id)

