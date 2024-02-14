from dto.model import ProductGroups
from tables.database import ProductGroups as Database
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(Database).filter(Database.ID == user_id).first()

def create_task(db: Session, data: ProductGroups):
    try:
        exp = Database(Parent_ID = data.Parent_ID, 
                    Group_Code = data.Group_Code, 
                    Name = data.Name, 
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

def update_task(db: Session, data: ProductGroups, id: int):
    try:
        exp = db.query(Database).filter(Database.ID == id).first()
        exp.Parent_ID = data.Parent_ID
        exp.Group_Code = data.Group_Code
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
    exp = db.query(Database).filter(Database.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp