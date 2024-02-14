

from fastapi import APIRouter
from database import db
from operations.ddm import get_task, create_task, delete_task, update_task
from dto.model import DocumentTypesDDM 


router = APIRouter()

@router.get('/documentTypesDDM/')
async def get_products(id : int):
    return get_task(db,id)

@router.post('/documentTypesDDM/')
async def post_products(data : DocumentTypesDDM):
    return create_task(db,data)


@router.put('/documentTypesDDM/')
async def put_products(id : int, data : DocumentTypesDDM):
    return update_task(db,id,data)

@router.delete('/documentTypesDDM/')
async def del_products(id : int):
    return delete_task(db, id)

