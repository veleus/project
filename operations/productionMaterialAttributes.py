from dto.model import ProductionMaterialAttributes as model

from tables.database import ProductionMaterialAttributes

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialAttributes).filter(ProductionMaterialAttributes.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionMaterialAttributes(ID_Material = data.ID_Material, 
                                            Attribute_Name = data.Attribute_Name, 
                                            Attribute_Value = data.Attribute_Value)
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
        exp = db.query(ProductionMaterialAttributes).filter(ProductionMaterialAttributes.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Attribute_Name = data.Attribute_Name
        exp.Attribute_Value = data.Attribute_Value
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialAttributes).filter(ProductionMaterialAttributes.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp