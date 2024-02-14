from dto.model import ProductionMaterialAvailability as Material
from tables.database import ProductionMaterialAvailability
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(ProductionMaterialAvailability).filter(ProductionMaterialAvailability.ID == user_id).first()

def create_task(db: Session, data: Material):
    try:
        exp = ProductionMaterialAvailability(ID_Material = data.ID_Material,
                                            Warehouse_Availability = data.Warehouse_Availability, 
                                            In_Transit = data.In_Transit,
                                            Reserved = data.Reserved)
        db.add(exp)
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def update_task(db: Session, data: Material, id: int):
    try:
        exp = db.query(ProductionMaterialAvailability).filter(ProductionMaterialAvailability.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Warehouse_Availability = data.Warehouse_Availability
        exp.In_Transit = data.In_Transit
        exp.Reserved = data.Reserved
        db.commit()
        db.refresh()
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialAvailability).filter(ProductionMaterialAvailability.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp