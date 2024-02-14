from fastapi import APIRouter
from database import db
from dto.model import ProductionMaterialSuppliers
from operations.productionmaterialsuppliers import get_task, create_task, delete_task, update_task
router = APIRouter()

@router.get('/productionMaterialSuppliers/')
async def get_productgroups(id: int):
    return get_task(db,id)

@router.post('/productionMaterialSuppliers/')
async def post_productgroups(data: ProductionMaterialSuppliers):
    return create_task(db,data)

@router.put('/productionMaterialSuppliers/')
async def put_productgroups(data: ProductionMaterialSuppliers, id: int):
    return update_task(db,data,id)

@router.delete('/productionMaterialSuppliers/')
async def del_productgroups(id: int):
    return delete_task(db,id)

