from sqlalchemy.orm import Session
from tables.database import ProductionMaterialCategories 
from dto.model import ProductionMaterialCategories as Model
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, user_id:int):
    return db.query(ProductionMaterialCategories).filter(ProductionMaterialCategories.ID == user_id).first()


def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialCategories(ID_Material = data.ID_Material, 
                                        Category_Name = data.Category_Name)
        
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
        exp = db.query(ProductionMaterialCategories).filter(ProductionMaterialCategories.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Category_Name = data.Category_Name
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
        
def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialCategories).filter(ProductionMaterialCategories.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp