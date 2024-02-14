from dto.model import ProductionMaterialSuppliers as Model
from tables.database import ProductionMaterialSuppliers
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionMaterialSuppliers).filter(ProductionMaterialSuppliers.ID == user_id).first()


def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialSuppliers(ID_Material = data.ID_Material, 
                                        ID_Supplier = data.ID_Supplier)
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
        exp = db.query(ProductionMaterialSuppliers).filter(ProductionMaterialSuppliers.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.ID_Supplier = data.ID_Supplier
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialSuppliers).filter(ProductionMaterialSuppliers.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp