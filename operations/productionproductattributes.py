from dto.model import ProductionProductAttributes as model
from tables.database import ProductionProductAttributes
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductAttributes).filter(ProductionProductAttributes.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductAttributes(ID_Product = data.ID_Product, 
                                        Attribute_Name = data.Attribute_Name, 
                                        Attribute_Value = data.Attribute_Value)
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
        exp = db.query(ProductionProductAttributes).filter(ProductionProductAttributes.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Attribute_Name = data.Attribute_Name
        exp.Attribute_Value = data.Attribute_Value
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductAttributes).filter(ProductionProductAttributes.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp