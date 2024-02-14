from dto.model import ProductionEmployeeSkills as Skills
from tables.database import ProductionEmployeeSkills
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionEmployeeSkills).filter(ProductionEmployeeSkills.ID == id).first()

def create_task(db: Session, data: Skills):
    try:
        exp = ProductionEmployeeSkills(ID_User = data.ID_User, 
                                    Skill_Name = data.Skill_Name,
                                    Skill_Level = data.Skill_Level)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: Skills, id: int):
    try:
        exp = db.query(ProductionEmployeeSkills).filter(ProductionEmployeeSkills.ID == id).first()
        exp.ID_User = data.ID_User
        exp.Skill_Name = data.Skill_Name
        exp.Skill_Level = data.Skill_Level
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionEmployeeSkills).filter(ProductionEmployeeSkills.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp