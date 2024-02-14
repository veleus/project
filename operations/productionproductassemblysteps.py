from dto.model import ProductionProductAssemblySteps as model
from tables.database import ProductionProductAssemblySteps
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


def get_task(db: Session, id: int):
    return db.query(ProductionProductAssemblySteps).filter(ProductionProductAssemblySteps.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductAssemblySteps(ID_WorkOrderItem = data.ID_WorkOrderItem, 
                                            Step_Number = data.Step_Number,
                                            Description = data.Description,
                                            Estimated_Duration = data.Estimated_Duration,
                                            Actual_Start_Date = data.Actual_Start_Date,
                                            Actual_End_Date = data.Actual_End_Date,
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
        exp = db.query(ProductionProductAssemblySteps).filter(ProductionProductAssemblySteps.ID == id).first()
        exp.ID_WorkOrderItem = data.ID_WorkOrderItem
        exp.Step_Number = data.Step_Number
        exp.Description = data.Description
        exp.Estimated_Duration = data.Estimated_Duration
        exp.Actual_Start_Date = data.Actual_Start_Date
        exp.Actual_End_Date = data.Actual_End_Date
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
    exp = db.query(ProductionProductAssemblySteps).filter(ProductionProductAssemblySteps.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp