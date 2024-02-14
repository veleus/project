from dto.model import ReadnisStagesToMaterial as model

from tables.database import ReadnisStagesToMaterial
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(ReadnisStagesToMaterial).filter(ReadnisStagesToMaterial.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ReadnisStagesToMaterial(ID_ProdExe = data.ID_ProdExe, 
                                    ID_Material = data.ID_Material, 
                                    Prod_Quantity = data.Prod_Quantity)
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
        exp = db.query(ReadnisStagesToMaterial).filter(ReadnisStagesToMaterial.ID == id).first()
        exp.ID_ProdExe = data.ID_ProdExe
        exp.ID_Material = data.ID_Material
        exp.Prod_Quantity = data.Prod_Quantity
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
def delete_task(db: Session, id: int):
    exp = db.query(ReadnisStagesToMaterial).filter(ReadnisStagesToMaterial.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp