from dto.model import ProductionDefects as Production
from tables.database import ProductionDefects 
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(ProductionDefects).filter(ProductionDefects.ID == user_id).first()

def create_task(db: Session, data: Production):
    try:
        exp = ProductionDefects(ID_WorkOrderItem = data.ID_WorkOrderItem, 
                                Quantity = data.Quantity, 
                                Date = data.Date,
                                Reason = data.Reason,
                                Description = data.Description)
        db.add(exp)
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: Production, id: int):
    try:
        exp = db.query(ProductionDefects).filter(ProductionDefects.ID == id).first()
        exp.ID_WorkOrderItem = data.ID_WorkOrderItem
        exp.Quantity = data.Quantity
        exp.Date = data.Date
        exp.Reason = data.Reason
        exp.Description = data.Description
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionDefects).filter(ProductionDefects.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

