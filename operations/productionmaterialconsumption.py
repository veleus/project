from dto.model import ProductionMaterialConsumption as Model
from tables.database import ProductionMaterialConsumption
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionMaterialConsumption).filter(ProductionMaterialConsumption.ID == user_id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialConsumption(ID_WorkOrderItem = data.ID_WorkOrderItem, 
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

def update_task(db: Session, data: Model, id: int):
    try:
        exp = db.query(ProductionMaterialConsumption).filter(ProductionMaterialConsumption.ID == id).first()
        exp.ID_WorkOrderItem = data.ID_WorkOrderItem
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
    exp = db.query(ProductionMaterialConsumption).filter(ProductionMaterialConsumption.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp