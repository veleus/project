from dto.model import ProductionQualityControl as model

from tables.database import ProductionQualityControl

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionQualityControl).filter(ProductionQualityControl.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionQualityControl(ID_Product = data.ID_Product, 
                                    Date = data.Date, 
                                    Inspector = data.Inspector, 
                                    Status = data.Status, 
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
        exp = db.query(ProductionQualityControl).filter(ProductionQualityControl.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Date = data.Date
        exp.Inspector = data.Inspector
        exp.Status = data.Status
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
    exp = db.query(ProductionQualityControl).filter(ProductionQualityControl.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp


