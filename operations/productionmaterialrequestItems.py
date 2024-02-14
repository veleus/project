from dto.model import ProductionMaterialRequestItems as Model
from tables.database import ProductionMaterialRequestItems
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionMaterialRequestItems).filter(ProductionMaterialRequestItems.ID == user_id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialRequestItems(ID_Request = data.ID_Request, 
                                            ID_Material = data.ID_Material, 
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

def update_task(db: Session, data: Model, id: int):
    try:
        exp = db.query(ProductionMaterialRequestItems).filter(ProductionMaterialRequestItems.ID == id).first()
        exp.ID_Request = data.ID_Request
        exp.ID_Material = data.ID_Material
        exp.Quantity = data.Quantity
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialRequestItems).filter(ProductionMaterialRequestItems.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

