from dto.model import ProductionMaterialTransfers as model
from tables.database import ProductionMaterialTransfers
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialTransfers).filter(ProductionMaterialTransfers.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionMaterialTransfers(ID_Material = data.ID_Material, 
                                        From_Warehouse = data.From_Warehouse, 
                                        To_Warehouse = data.Quantity,
                                        Date = data.Date,
                                        Reason = data.Reason)
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
        exp = db.query(ProductionMaterialTransfers).filter(ProductionMaterialTransfers.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.From_Warehouse = data.From_Warehouse
        exp.To_Warehouse = data.To_Warehouse
        exp.Date = data.Date
        exp.Reason = data.Reason
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    try:
        exp = db.query(ProductionMaterialTransfers).filter(ProductionMaterialTransfers.ID == id).first()
        db.delete(exp)
        db.commit()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()