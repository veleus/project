from dto.model import StagesToMaterial as model
from sqlalchemy.exc import SQLAlchemyError
from tables.database import StagesToMaterial
from sqlalchemy.orm import Session
def get_task(db: Session, user_id:int):
    return db.query(StagesToMaterial).filter(StagesToMaterial.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = StagesToMaterial(ID_Stages = data.ID_Stages, 
                                ID_Material = data.ID_Material, 
                                Quantity = data.Quantity)
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
        exp = db.query(StagesToMaterial).filter(StagesToMaterial.ID == id).first()
        exp.ID_Stages = data.ID_Stages
        exp.ID_Material = data.ID_Material
        exp.Quantity = data.Quantity
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(StagesToMaterial).filter(StagesToMaterial.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
