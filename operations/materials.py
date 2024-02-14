from dto.model import Materials as model

from tables.database import Materials

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(Materials).filter(Materials.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = Materials(Name = data.Name, 
                    Description = data.Description)
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
        exp = db.query(Materials).filter(Materials.ID == id).first()
        exp.Name = data.Name
        exp.Description = data.Description
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    try:
        exp = db.query(Materials).filter(Materials.ID == id).first()
        db.delete(exp)
        db.commit()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
        