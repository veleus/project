from dto.model import ProductionProductDefects as model
from tables.database import ProductionProductDefects
from sqlalchemy.orm import Session 
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductDefects).filter(ProductionProductDefects.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductDefects(ID_Product = data.ID_Product, 
                                    Quantity = data.Quantity, 
                                    Date = data.Date, 
                                    Reason = data.Reason,
                                    Description = data.Description)
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
        exp = db.query(ProductionProductDefects).filter(ProductionProductDefects.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Quantity = data.Quantity
        exp.Date = data.Date
        exp.Reason = data.Reason
        exp.Description = data.Description
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductDefects).filter(ProductionProductDefects.ID == id).first()
    db.delete(exp)
    db.commit()