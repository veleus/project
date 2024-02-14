from dto.model import ProductionProductSupplierContacts as model
from tables.database import ProductionProductSupplierContacts
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductSupplierContacts).filter(ProductionProductSupplierContacts.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductSupplierContacts(ID_Supplier = data.ID_Supplier, 
                                                Contact_Type = data.Contact_Type, 
                                                Contact_Value = data.Contact_Value)
        db.add(exp)
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: model, id: int):
    try:
        exp = db.query(ProductionProductSupplierContacts).filter(ProductionProductSupplierContacts.ID == id).first()
        exp.ID_Supplier = data.ID_Supplier
        exp.Contact_Type = data.Contact_Type
        exp.Contact_Value = data.Contact_Value
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductSupplierContacts).filter(ProductionProductSupplierContacts.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp