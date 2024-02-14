from dto.model import ProductionMaterialSurplus as model
from tables.database import ProductionMaterialSurplus
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionMaterialSurplus).filter(ProductionMaterialSurplus.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionMaterialSurplus(ID_WorkOrderItem = data.ID_WorkOrderItem, 
                                        ID_Material = data.ID_Material, 
                                        Quantity_Surplus = data.Quantity_Surplus,
                                        Date = data.Date,
                                        Reason = data.Reason,
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

def update_task(db: Session, data : model , id: int):
    exp = db.query(ProductionMaterialSurplus).filter(ProductionMaterialSurplus.ID == id).first()
    exp.ID_WorkOrderItem = data.ID_WorkOrderItem
    exp.ID_Material = data.ID_Material
    exp.Quantity_Surplus = data.Quantity_Surplus
    exp.Date = data.Date
    exp.Reason = data.Reason
    exp.Description = data.Description
    db.commit()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialSurplus).filter(ProductionMaterialSurplus.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp