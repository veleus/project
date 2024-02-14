from dto.model import ProductionMaterialCosts as Model
from tables.database import ProductionMaterialCosts
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError  

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialCosts).filter(ProductionMaterialCosts.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialCosts(ID_Material = data.ID_Material, 
                                    Cost = data.Cost, 
                                    Date = data.Date,
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


def update_task(db: Session, data: Model, id: int):
    try:
        exp = db.query(ProductionMaterialCosts).filter(ProductionMaterialCosts.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Cost = data.Cost
        exp.Date = data.Date
        exp.Description = data.Description
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialCosts).filter(ProductionMaterialCosts.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp