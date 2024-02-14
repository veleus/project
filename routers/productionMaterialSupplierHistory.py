from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialSupplierContacts
from operations.productionmaterialsupplierhistory import get_task, create_task, update_task, delete_task
router = APIRouter()

@router.get('/productionMaterialSupplierHistory/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionMaterialSupplierHistory/')
async def post_productgroups(data: ProductionMaterialSupplierContacts):
    return create_task(db, data)

@router.put('/productionMaterialSupplierHistory/')
async def put_productgroups(data: ProductionMaterialSupplierContacts, id: int):
    return update_task(db, data, id)

@router.delete('/productionMaterialSupplierHistory/')
async def del_productgroups(id : int):
    return delete_task(db, id)

