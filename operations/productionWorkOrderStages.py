from dto.model import ProductionWorkOrderStages as model

from tables.database import ProductionWorkOrderStages

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):

    return db.query(ProductionWorkOrderStages).filter(ProductionWorkOrderStages.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionWorkOrderStages(ID_WorkOrderItem = data.ID_WorkOrderItem, 
                                        ID_Stage = data.ID_Stage, 
                                        Start_Date = data.Start_Date,
                                        End_Date = data.End_Date,
                                        Status = data.Status)
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
        exp = db.query(ProductionWorkOrderStages).filter(ProductionWorkOrderStages.ID == id).first()
        exp.ID_WorkOrderItem = data.ID_WorkOrderItem
        exp.ID_Stage = data.ID_Stage
        exp.Start_Date = data.Start_Date
        exp.End_Date = data.End_Date
        exp.Status = data.Status
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionWorkOrderStages).filter(ProductionWorkOrderStages.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp