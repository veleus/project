from dto.model import ProductionMaterialUsage as model
from tables.database import ProductionMaterialUsage
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionMaterialUsage).filter(ProductionMaterialUsage.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionMaterialUsage(ID_ProdExec = data.ID_ProdExec, 
                                    ID_Material = data.ID_Material, 
                                    Quantity_Used = data.Quantity_Used,
                                    Date = data.Date)
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
        exp = db.query(ProductionMaterialUsage).filter(ProductionMaterialUsage.ID == id).first()
        exp.ID_ProdExec = data.ID_ProdExec
        exp.ID_Material = data.ID_Material
        exp.Quantity_Used = data.Quantity_Used
        exp.Date = data.Date
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialUsage).filter(ProductionMaterialUsage.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp