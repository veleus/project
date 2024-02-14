from dto.model import ProductionMaterialReturnsReasons as Model
from sqlalchemy.exc import SQLAlchemyError
from tables.database import ProductionMaterialReturnsReasons
from sqlalchemy.orm import Session


def get_task(db: Session, id: int):
    return db.query(ProductionMaterialReturnsReasons).filter(ProductionMaterialReturnsReasons.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialReturnsReasons(ID_Material = data.ID_Material, 
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

def update_task(db: Session, data: Model, id: int):
    try:
        exp = db.query(ProductionMaterialReturnsReasons).filter(ProductionMaterialReturnsReasons.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Reason_Name = data.Reason_Name
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
    exp = db.query(ProductionMaterialReturnsReasons).filter(ProductionMaterialReturnsReasons.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp