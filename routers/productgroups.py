from fastapi import APIRouter
from database import db
from dto.model import ProductGroups
from operations.productsgroups import create_task, get_task, delete_task, update_task
router = APIRouter()

@router.get('/productgroups/')
async def get_productgroups(id):
    return get_task(db,id)

@router.post('/productgroups/')
async def post_productgroups(data : ProductGroups):
    return create_task(db,data)
@router.put('/productgroups/')
async def put_productgroups(data : ProductGroups, id : int):
    return update_task(db,data,id)

@router.delete('/productgroups/')
async def del_productgroups(id : int):
    return delete_task(db,id)

