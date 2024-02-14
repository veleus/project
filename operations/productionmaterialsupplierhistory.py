from dto.model import ProductionMaterialSupplierContacts as Model
from tables.database import ProductionMaterialSupplierContacts 
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


def get_task(db: Session, id: int):
    return db.query(ProductionMaterialSupplierContacts).filter(ProductionMaterialSupplierContacts.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialSupplierContacts(ID_Supplier = data.ID_Supplier, 
                                            Contact_Type = data.Contact_Type, 
                                            Contact_Value = data.Contact_Value)
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
    exp = db.query(ProductionMaterialSupplierContacts).filter(ProductionMaterialSupplierContacts.ID == id).first()
    exp.ID_Supplier = data.ID_Supplier
    exp.Contact_Type = data.Contact_Type
    exp.Contact_Value = data.Contact_Value
    db.commit()
    db.refresh(exp)
    return exp

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialSupplierContacts).filter(ProductionMaterialSupplierContacts.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp