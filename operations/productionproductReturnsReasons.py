from dto.model import ProductionProductReturnsReasons as model
from tables.database import ProductionProductReturnsReasons
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):

    return db.query(ProductionProductReturnsReasons).filter(ProductionProductReturnsReasons.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductReturnsReasons(ID_Product = data.ID_Product, 
                                            Reason_Name = data.Reason_Name, 
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
        exp = db.query(ProductionProductReturnsReasons).filter(ProductionProductReturnsReasons.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Reason_Name = data.Reason_Name
        exp.Description = data.Description
        db.commit()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductReturnsReasons).filter(ProductionProductReturnsReasons.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
