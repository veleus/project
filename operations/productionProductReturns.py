from dto.model import ProductionProductReturns as model
from tables.database import ProductionProductReturns
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductReturns).filter(ProductionProductReturns.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductReturns(ID_Product = data.ID_Product, 
                                    Date = data.Date, 
                                    Quantity = data.Quantity, 
                                    Return_Reason = data.Return_Reason,
                                    Comments = data.Comments)
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
        exp = db.query(ProductionProductReturns).filter(ProductionProductReturns.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Date = data.Date
        exp.Quantity = data.Quantity
        exp.Return_Reason = data.Return_Reason
        exp.Comments = data.Comments
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductReturns).filter(ProductionProductReturns.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp