from dto.model import Stages as model

from tables.database import Stages
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

def get_task(db: Session, user_id:int):
    return db.query(Stages).filter(Stages.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = Stages(Name = data.Name,
                    Description = data.Description,
                    ID_TechMap = data.ID_TechMap,
                    Num = data.Num,
                    Exec_time = data.Exec_time,
                    Cost = data.Cost)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: model):
    try:
        exp = db.query(Stages).filter(Stages.ID == data.ID).first()
        exp.Name = data.Name
        exp.Description = data.Description
        exp.ID_TechMap = data.ID_TechMap
        exp.Num = data.Num
        exp.Exec_time = data.Exec_time
        exp.Cost = data.Cost
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Stages).filter(Stages.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

