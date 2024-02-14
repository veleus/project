from dto.model import SupplierOrders as model

from tables.database import SupplierOrders

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, id: int):
    return db.query(SupplierOrders).filter(SupplierOrders.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = SupplierOrders(ID_Supplier = data.ID_Supplier,
                            Creation_Date = data.Creation_Date,
                            Order_Number = data.Order_Number,
                            Status_ID = data.Status_ID,
                            Paid = data.Paid,
                            Delivery_Date = data.Delivery_Date)
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
        exp = db.query(SupplierOrders).filter(SupplierOrders.ID == id).first()
        exp.ID_Supplier = data.ID_Supplier
        exp.Creation_Date = data.Creation_Date
        exp.Order_Number = data.Order_Number
        exp.Status_ID = data.Status_ID
        exp.Paid = data.Paid
        exp.Delivery_Date = data.Delivery_Date
        db.commit()

        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(SupplierOrders).filter(SupplierOrders.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

