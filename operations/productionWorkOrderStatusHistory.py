from dto.model import ProductionWorkOrderStatusHistory as model
from tables.database import ProductionWorkOrderStatusHistory
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, id: int):
    return db.query(ProductionWorkOrderStatusHistory).filter(ProductionWorkOrderStatusHistory.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionWorkOrderStatusHistory(ID_WorkOrder = data.ID_WorkOrder, 
                                                Status = data.Status, 
                                                Date = data.Date)
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
        exp = db.query(ProductionWorkOrderStatusHistory).filter(ProductionWorkOrderStatusHistory.ID == id).first()
        exp.ID_WorkOrder = data.ID_WorkOrder
        exp.Status = data.Status
        exp.Date = data.Date
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionWorkOrderStatusHistory).filter(ProductionWorkOrderStatusHistory.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp