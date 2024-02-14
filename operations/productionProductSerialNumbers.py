from dto.model import ProductionProductSerialNumbers as model
from tables.database import ProductionProductSerialNumbers
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductSerialNumbers).filter(ProductionProductSerialNumbers.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductSerialNumbers(ID_Product = data.ID_Product, 
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


def update_task(db: Session, data: model, id: int):
    try:
        exp = db.query(ProductionProductSerialNumbers).filter(ProductionProductSerialNumbers.ID == id).first()
        exp.ID_Product = data.ID_Product
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
    exp = db.query(ProductionProductSerialNumbers).filter(ProductionProductSerialNumbers.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp