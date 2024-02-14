from dto.model import Suppliers as model

from tables.database import Suppliers

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(Suppliers).filter(Suppliers.ID == id).first()

def create_task(db: Session, data: model):
    try:

        exp = Suppliers(Warehouse_ID = data.Warehouse_ID, 
                        Name = data.Name, 
                        Phone = data.Phone, 
                        Address = data.Address, 
                        Email = data.Email, 
                        INN = data.INN, 
                        Contact_Manager = data.Contact_Manager, 
                        Delivery_Time = data.Delivery_Time, 
                        Country = data.Country)
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
        exp = db.query(Suppliers).filter(Suppliers.ID == id).first()
        exp.Warehouse_ID = data.Warehouse_ID
        exp.Name = data.Name
        exp.Phone = data.Phone
        exp.Address = data.Address
        exp.Email = data.Email
        exp.INN = data.INN
        exp.Contact_Manager = data.Contact_Manager
        exp.Delivery_Time = data.Delivery_Time
        exp.Country = data.Country
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Suppliers).filter(Suppliers.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp