from dto.model import ProductionTask as model
from tables.database import ProductionTask
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionTask).filter(ProductionTask.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionTask(Date = data.Date, 
                            Warehouse_Materials = data.Warehouse_Materials, 
                            Warehouse_Products = data.Warehouse_Products, 
                            ID_TechMap = data.ID_TechMap, 
                            Quantity = data.Quantity)
        db.add(exp)

        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: model, id: int):
    try:
        exp = db.query(ProductionTask).filter(ProductionTask.ID == id).first()
        exp.Date = data.Date
        exp.Warehouse_Materials = data.Warehouse_Materials
        exp.Warehouse_Products = data.Warehouse_Products
        exp.ID_TechMap = data.ID_TechMap
        exp.Quantity = data.Quantity
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionTask).filter(ProductionTask.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp