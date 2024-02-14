from dto.model import MaterialMovementItems
from tables.database import MaterialMovementItems as Database
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError  

def get_task(db: Session, user_id:int):
    return db.query(Database).filter(Database.ID == user_id).first()


def create_task(db: Session, data: MaterialMovementItems):
    try:
        exp = Database(ID_Movement = data.ID_Movement, ID_Product = data.ID_Product, Quantity = data.Quantity, Comment = data.Comment)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: MaterialMovementItems, id: int):
    try:
        exp = db.query(Database).filter(Database.ID == id).first()
        exp.ID_Movement = data.ID_Movement
        exp.ID_Product = data.ID_Product
        exp.Quantity = data.Quantity
        exp.Comment = data.Comment
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Database).filter(Database.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp