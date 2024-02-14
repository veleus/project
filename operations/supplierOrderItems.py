from dto.model import SupplierOrderItems as model
from tables.database import SupplierOrderItems
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(SupplierOrderItems).filter(SupplierOrderItems.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = SupplierOrderItems(
                                ID_Order = data.ID_Order, 
                                ID_Product = data.ID_Product, 
                                Quantity = data.Quantity)
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

    exp = db.query(SupplierOrderItems).filter(SupplierOrderItems.ID == id).first()
    exp.ID_Order = data.ID_Order
    exp.ID_Product = data.ID_Product
    exp.Quantity = data.Quantity
    db.commit()
    db.refresh(exp)
    return exp


def delete_task(db: Session, id: int):
    exp = db.query(SupplierOrderItems).filter(SupplierOrderItems.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
