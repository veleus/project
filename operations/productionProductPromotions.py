from dto.model import ProductionProductPromotions as model
from tables.database import ProductionProductPromotions
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductPromotions).filter(ProductionProductPromotions.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductPromotions(ID_Product = data.ID_Product, 
                                        Promotion_Name = data.Promotion_Name, 
                                        Start_Date = data.Start_Date,
                                        End_Date = data.End_Date,
                                        Discount_Percentage = data.Discount_Percentage)
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
        exp = db.query(ProductionProductPromotions).filter(ProductionProductPromotions.ID == id).first()
        exp.ID_Product = data.ID_Product
        exp.Promotion_Name = data.Promotion_Name
        exp.Start_Date = data.Start_Date
        exp.End_Date = data.End_Date
        exp.Discount_Percentage = data.Discount_Percentage
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductPromotions).filter(ProductionProductPromotions.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

