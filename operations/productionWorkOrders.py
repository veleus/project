from dto.model import ProductionWorkOrders as model

from tables.database import ProductionWorkOrders
from sqlalchemy.orm import Session

def get_task(db: Session, id: int):
    return db.query(ProductionWorkOrders).filter(ProductionWorkOrders.ID == id).first()

from sqlalchemy.exc import SQLAlchemyError

def create_task(db: Session, data: ProductionWorkOrders):
    try:
        exp = ProductionWorkOrders(
                                    ID_User=data.ID_User, 
                                   Date_Assigned=data.Date_Assigned, 
                                   Planned_Start_Date=data.Planned_Start_Date, 
                                   Planned_End_Date=data.Planned_End_Date, 
                                   Status=data.Status, 
                                   Actual_Start_Date=data.Actual_Start_Date, 
                                   Actual_End_Date=data.Actual_End_Date, 
                                   Reason_Cancelled=data.Reason_Cancelled)
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
        exp = db.query(ProductionWorkOrders).filter(ProductionWorkOrders.ID == id).first()
        exp.ID_User = data.ID_User
        exp.Date_Assigned = data.Date_Assigned
        exp.Planned_Start_Date = data.Planned_Start_Date
        exp.Planned_End_Date = data.Planned_End_Date
        exp.Status = data.Status
        exp.Actual_Start_Date = data.Actual_Start_Date
        exp.Actual_End_Date = data.Actual_End_Date
        exp.Reason_Cancelled = data.Reason_Cancelled
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionWorkOrders).filter(ProductionWorkOrders.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
