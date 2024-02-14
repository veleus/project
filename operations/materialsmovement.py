from dto.model import MaterialMovements
from tables.database import MaterialMovements as Material
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(Material).filter(Material.ID == user_id).first()

def create_task(db: Session, data: MaterialMovements):
    try:
        exp = Material(Document_Type = data.Document_Type, 
                    Document_Base_Number = data.Document_Base_Number, 
                    Receipt_Date = data.Receipt_Date, 
                    ID_Contractor = data.ID_Contractor,
                        ID_Employee = data.ID_Employee )
        db.add(exp)
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: MaterialMovements, id: int):
    try:
        exp = db.query(Material).filter(Material.ID == id).first()
        exp.Document_Type = data.Document_Type
        exp.Document_Base_Number = data.Document_Base_Number
        exp.Receipt_Date = data.Receipt_Date
        exp.ID_Contractor = data.ID_Contractor
        exp.ID_Employee = data.ID_Employee
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Material).filter(Material.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp