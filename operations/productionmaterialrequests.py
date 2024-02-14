from dto.model import ProductionMaterialRequests as Model
from tables.database import ProductionMaterialRequests
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialRequests).filter(ProductionMaterialRequests.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialRequests(ID_User = data.ID_User, 
                                        Date = data.Date, 
                                        Status = data.Status,
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

def update_task(db: Session, data: Model):
    try:
        exp = db.query(ProductionMaterialRequests).filter(ProductionMaterialRequests.ID == data.ID).first()
        exp.ID_User = data.ID_User
        exp.Date = data.Date
        exp.Status = data.Status
        exp.Description = data.Description
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialRequests).filter(ProductionMaterialRequests.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp


