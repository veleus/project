from dto.model import ProductionProductCategories as model
from tables.database import ProductionProductCategories
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductCategories).filter(ProductionProductCategories.ID == user_id).first()

def create_task(db: Session, data: model):
    try:

        exp = ProductionProductCategories(ID_Product = data.ID_Product, 
                                        Category_Name = data.Category_Name)
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
        exp = db.query(ProductionProductCategories).filter(ProductionProductCategories.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Category_Name = data.Category_Name
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductCategories).filter(ProductionProductCategories.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp