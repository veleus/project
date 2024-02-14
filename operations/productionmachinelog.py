from dto.model import ProductionMachineLog as Production
from tables.database import ProductionMachineLog
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMachineLog).filter(ProductionMachineLog.ID == id).first()

def create_task(db: Session, data: Production):
    try:
        exp = ProductionMachineLog(Machine_ID = data.Machine_ID, 
                                Date = data.Date,
                                Operation_Performed = data.Operation_Performed,
                                Operator = data.Operator,
                                Status = data.Status)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: Production, id: int):
    try:
        exp = db.query(ProductionMachineLog).filter(ProductionMachineLog.ID == id).first()
        exp.Machine_ID = data.Machine_ID
        exp.Date = data.Date
        exp.Operation_Performed = data.Operation_Performed
        exp.Operator = data.Operator
        exp.Status = data.Status
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMachineLog).filter(ProductionMachineLog.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
