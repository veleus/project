from dto.model import ProductionMaterialDefects as Model
from tables.database import ProductionMaterialDefects
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialDefects).filter(ProductionMaterialDefects.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialDefects(ID_Material = data.ID_Material, 
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


def update_task(db: Session, data: Model, id: int):
    try:
        exp = db.query(ProductionMaterialDefects).filter(ProductionMaterialDefects.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Quantity = data.Quantity
        exp.Date = data.Date
        exp.Reason = data.Reason
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
    exp = db.query(ProductionMaterialDefects).filter(ProductionMaterialDefects.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp