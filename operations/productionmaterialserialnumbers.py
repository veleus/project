from dto.model import ProductionMaterialSerialNumbers as Model
from tables.database import ProductionMaterialSerialNumbers
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialSerialNumbers).filter(ProductionMaterialSerialNumbers.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialSerialNumbers(ID_Material = data.ID_Material, 
                                            Serial_Number = data.Serial_Number)
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
        exp = db.query(ProductionMaterialSerialNumbers).filter(ProductionMaterialSerialNumbers.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Serial_Number = data.Serial_Number
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialSerialNumbers).filter(ProductionMaterialSerialNumbers.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp