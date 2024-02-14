
from dto.model import Role as model
from tables.database import Role
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


def get_task(db: Session, user_id:str):
    return db.query(Role).filter(Role.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = Role(Role=data.role)
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
        exp = db.query(Role).filter(Role.ID == id).first()
        exp.ID = data.ID
        exp.Role = data.role
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Role).filter(Role.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
