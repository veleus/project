from sqlalchemy.orm import Session
from dto.model import ProductionMachineMaintenance as ProductionMaintenance
from tables.database import ProductionMachineMaintenance
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMachineMaintenance).filter(ProductionMachineMaintenance.ID == id).first()

def create_task(db: Session, data: ProductionMaintenance):
    try:
        exp = ProductionMachineMaintenance(
                                        ID_Machine = data.ID_Machine, 
                                        Date = data.Date, 
                                        Maintenance_Type = data.Maintenance_Type, 
                                        Description = data.Description,
                                        Cost = data.Cost)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: ProductionMaintenance):
    try:
        exp = db.query(ProductionMachineMaintenance).filter(ProductionMachineMaintenance.ID == data.ID).first()
        exp.ID_Machine = data.ID_Machine
        exp.Date = data.Date
        exp.Maintenance_Type = data.Maintenance_Type
        exp.Description = data.Description
        exp.Cost = data.Cost
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionMachineMaintenance).filter(ProductionMachineMaintenance.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

