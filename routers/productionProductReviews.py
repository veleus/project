from fastapi import APIRouter
from operations.productionProductReviews import create_task, get_task, update_task, delete_task
from dto.model import ProductionProductReviews
from database import db 
router = APIRouter()

@router.get('/productionProductReviews/')
async def get_productgroups(id: int):
    return get_task(db, id)

@router.post('/productionProductReviews/')
async def post_productgroups(data: ProductionProductReviews):
    return create_task(db, data)

@router.put('/productionProductReviews/')
async def put_productgroups(data: ProductionProductReviews, id: int):
    return update_task(db, data, id)

@router.delete('/productionProductReviews/')
async def del_productgroups(id: int):
    return delete_task(db, id)

