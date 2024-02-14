from dto.model import ProductionProductWarranty as model
from tables.database import ProductionProductWarranty
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductWarranty).filter(ProductionProductWarranty.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductWarranty(ID_Product = data.ID_Product, 
                                                Warranty_Period = data.Warranty_Period, 
                                                Warranty_Description = data.Warranty_Description)
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
        exp = db.query(ProductionProductWarranty).filter(ProductionProductWarranty.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Warranty_Period = data.Warranty_Period
        exp.Warranty_Description = data.Warranty_Description
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

    

def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductWarranty).filter(ProductionProductWarranty.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
