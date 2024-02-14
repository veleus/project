from fastapi import APIRouter
from operations.productionProductSupplierContacts import get_task, update_task, delete_task, create_task
from database import db
from dto.model import ProductionProductSupplierContacts
router = APIRouter()

@router.get('/productionProductSupplierContacts/')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionProductSupplierContacts/')
async def post_productgroups(data: ProductionProductSupplierContacts):
    return create_task(db,data)

@router.put('/productionProductSupplierContacts/')
async def put_productgroups(data: ProductionProductSupplierContacts, id: int):
    return  update_task(db,data, id)

@router.delete('/productionProductSupplierContacts/')
async def del_productgroups(id: int):
    return delete_task(db, id)

