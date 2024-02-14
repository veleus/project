from dto.model import Warehouse as model

from tables.database import Warehouse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(Warehouse).filter(Warehouse.Warehouse_ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = Warehouse(ID_Product = data.ID_Product,
                        Quantity = data.Quantity,
                        In_Transit = data.In_Transit,
                        Reserved = data.Reserved,
                        In_Production = data.In_Production)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: model):
    try:
        exp = db.query(Warehouse).filter(Warehouse.Warehouse_ID == data.ID).first()
        exp.ID_Product = data.ID_Product
        exp.Quantity = data.Quantity
        exp.In_Transit = data.In_Transit
        exp.Reserved = data.Reserved
        exp.In_Production = data.In_Production
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(Warehouse).filter(Warehouse.Warehouse_ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

