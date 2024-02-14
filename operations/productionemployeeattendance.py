from dto.model import ProductionEmployeeAttendance as Model
from tables.database import ProductionEmployeeAttendance
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionEmployeeAttendance).filter(ProductionEmployeeAttendance.ID == id).first()

def create_task(db: Session, data: Model):
    try: 
        exp = ProductionEmployeeAttendance(ID_User = data.ID_User, 
                                        Date = data.Date, 
                                        Attendance_Status = data.Attendance_Status)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: Model, id: int):
    try:
        exp = db.query(ProductionEmployeeAttendance).filter(ProductionEmployeeAttendance.ID == id).first()
        exp.ID_User = data.ID_User
        exp.Date = data.Date
        exp.Attendance_Status = data.Attendance_Status
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def deleate_task(db: Session, id: int):
    exp = db.query(ProductionEmployeeAttendance).filter(ProductionEmployeeAttendance.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
