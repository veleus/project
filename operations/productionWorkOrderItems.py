from dto.model import ProductionWorkOrderItems as model

from tables.database import ProductionWorkOrderItems

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionWorkOrderItems).filter(ProductionWorkOrderItems.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionWorkOrderItems(ID_WorkOrder = data.ID_WorkOrder, 
                                        ID_Product = data.ID_Product, 
                                        ID_Material = data.ID_Material, 
                                        Planned_Quantity = data.Planned_Quantity, 
                                        Actual_Quantity = data.Actual_Quantity, 
                                        Status = data.Status, 
                                        Reason_Cancelled = data.Reason_Cancelled)
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
        exp = db.query(ProductionWorkOrderItems).filter(ProductionWorkOrderItems.ID == id).first()
        exp.ID_WorkOrder = data.ID_WorkOrder
        exp.ID_Product = data.ID_Product
        exp.ID_Material = data.ID_Material
        exp.Planned_Quantity = data.Planned_Quantity
        exp.Actual_Quantity = data.Actual_Quantity
        exp.Status = data.Status
        exp.Reason_Cancelled = data.Reason_Cancelled
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionWorkOrderItems).filter(ProductionWorkOrderItems.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
