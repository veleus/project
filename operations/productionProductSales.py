from dto.model import ProductionProductSales as model
from tables.database import ProductionProductSales
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


def get_task(db: Session, user_id:int):
    return db.query(ProductionProductSales).filter(ProductionProductSales.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductSales(ID_Product = data.ID_Product, 
                                    Date = data.Date, 
                                    Quantity = data.Quantity, 
                                    Sale_Price = data.Sale_Price)
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
        exp = db.query(ProductionProductSales).filter(ProductionProductSales.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Date = data.Date
        exp.Quantity = data.Quantity
        exp.Sale_Price = data.Sale_Price
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductSales).filter(ProductionProductSales.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp