from dto.model import ProductionProductAssemblyLog as model
from tables.database import ProductionProductAssemblyLog
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(ProductionProductAssemblyLog).filter(ProductionProductAssemblyLog.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductAssemblyLog(ID_ProdExec = data.ID_ProdExec, 
                                        Assembly_Step = data.Assembly_Step,
                                            Date = data.Date,
                                            Employee = data.Employee,
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


def update_task(db: Session, data: model, id: int):
    try:
        exp = db.query(ProductionProductAssemblyLog).filter(ProductionProductAssemblyLog.ID == id).first()
        exp.ID_ProdExec = data.ID_ProdExec
        exp.Assembly_Step = data.Assembly_Step
        exp.Date = data.Date
        exp.Employee = data.Employee
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
    exp = db.query(ProductionProductAssemblyLog).filter(ProductionProductAssemblyLog.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp