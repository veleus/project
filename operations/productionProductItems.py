from dto.model import ProductionProductItems as model
from tables.database import ProductionProductItems
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductItems).filter(ProductionProductItems.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductItems(ID_TechMap = data.ID_TechMap, ID_Material = data.ID_Material, Value = data.Value)
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
        exp = db.query(ProductionProductItems).filter(ProductionProductItems.ID == id).first()
        exp.ID_TechMap = data.ID_TechMap
        exp.ID_Material = data.ID_Material
        exp.Value = data.Value
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductItems).filter(ProductionProductItems.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
