from dto.model import ProductionEmployeeProductivity
from tables.database import ProductionEmployeeProductivity as Productivity
from sqlalchemy.orm import Session  
from sqlalchemy.exc import SQLAlchemyError  

def get_task(db: Session, id: int):
    return db.query(Productivity).filter(Productivity.ID == id).first()


def create_task(db: Session, data: ProductionEmployeeProductivity):
    try:
        exp = Productivity(ID_User = data.ID_User, 
                        ID_WorkOrderItem = data.ID_WorkOrderItem, 
                        Productivity_Value = data.Productivity_Value,
                        Date_Recorded = data.Date_Recorded)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: ProductionEmployeeProductivity, id: int):
    try:
        exp = db.query(Productivity).filter(Productivity.ID == id).first()
        exp.ID_User = data.ID_User
        exp.ID_WorkOrderItem = data.ID_WorkOrderItem
        exp.Productivity_Value = data.Productivity_Value
        exp.Date_Recorded = data.Date_Recorded
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Productivity).filter(Productivity.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp