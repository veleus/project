from sqlalchemy.orm import Session
from dto.model import ProdExecution as execution
from tables.database import ProdExecution
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProdExecution).filter(ProdExecution.ID == user_id).first()

def create_task(db: Session, data: execution):
    try:
        exp = ProdExecution(ID_ProdTask = data.ID_ProdTask, 
                        ID_Stage = data.ID_Stage, 
                        ID_User = data.ID_User, 
                        Date_Start = data.Date_Start,
                        Quantity = data.Quantity,
                        Date_Finish = data.Date_Finish)
        db.add(exp)
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: execution, id: int):
    try:
        exp = db.query(ProdExecution).filter(ProdExecution.ID == id).first()
        exp.ID_ProdTask = data.ID_ProdTask
        exp.ID_Stage = data.ID_Stage
        exp.ID_User = data.ID_User
        exp.Date_Start = data.Date_Start
        exp.Quantity = data.Quantity
        exp.Date_Finish = data.Date_Finish
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProdExecution).filter(ProdExecution.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
