from dto.model import ProductionMaterialInventory as Model
from tables.database import ProductionMaterialInventory
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialInventory).filter(ProductionMaterialInventory.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialInventory(ID_Material = data.ID_Material, 
                                        Date = data.Date, 
                                        Actual_Quantity = data.Actual_Quantity,
                                        Comments = data.Comments)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: Model, id: int):
    try:
        exp = db.query(ProductionMaterialInventory).filter(ProductionMaterialInventory.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Date = data.Date
        exp.Actual_Quantity = data.Actual_Quantity
        exp.Comments = data.Comments
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialInventory).filter(ProductionMaterialInventory.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

