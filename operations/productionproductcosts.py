from dto.model import ProductionProductCosts as model
from tables.database import ProductionProductCosts
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionProductCosts).filter(ProductionProductCosts.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductCosts(ID_Product = data.ID_Product,
                                    Cost = data.Cost,
                                    Date = data.Date,
                                    Description= data.Description)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: model, task_id:int):
    try:

        exp = db.query(ProductionProductCosts).filter(ProductionProductCosts.ID == task_id).first()
        exp.ID_Product = data.ID_Product
        exp.Cost = data.Cost
        exp.Date = data.Date
        exp.Description = data.Description
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductCosts).filter(ProductionProductCosts.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
