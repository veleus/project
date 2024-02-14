from sqlalchemy.orm import Session
from dto.model import ProductionMaterialItems as model
from sqlalchemy.exc import SQLAlchemyError
from tables.database import ProductionMaterialItems


def get_task(db: Session, id: int):
    return db.query(ProductionMaterialItems).filter(ProductionMaterialItems.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionMaterialItems(ID_Material = data.ID_Material, 
                                    Value = data.Value)
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
        exp = db.query(ProductionMaterialItems).filter(ProductionMaterialItems.ID == id).first()
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
    exp = db.query(ProductionMaterialItems).filter(ProductionMaterialItems.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
