from dto.model import TechMap as model

from tables.database import TechMap

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(TechMap).filter(TechMap.Id == id).first()

def create_task(db: Session, data: model):
    try:
        exp = TechMap(Id = data.Id,
                    Name = data.Name,
                    ID_Material = data.ID_Material,
                    Comment = data.Comment)
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
    exp = db.query(TechMap).filter(TechMap.Id == id).first()
    exp.Id = data.Id
    exp.Name = data.Name
    exp.ID_Material = data.ID_Material
    exp.Comment = data.Comment
    db.commit()
    db.refresh(exp)
    return exp

def delete_task(db: Session, id: int):
    exp = db.query(TechMap).filter(TechMap.Id == id).first()
    db.delete(exp)
    db.commit()
    return exp
