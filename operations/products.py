from dto.model import Products as model
from tables.database import Products
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, id: int):
    return db.query(Products).filter(Products.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = Products(Group_ID = data.Group_ID, 
                    Nomenclature = data.Nomenclature, 
                    Supplier_id = data.Supplier_id,
                    Min_Quantity= data.Min_Quantity,
                    Article = data.Article,
                    External_Code = data.External_Code,
                    Unit_of_Measure = data.Unit_of_Measure,
                    Description = data.Description,
                    Cell = data.Cell)
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
        exp = db.query(Products).filter(Products.ID == id).first()
        exp.Group_ID = data.Group_ID
        exp.Nomenclature = data.Nomenclature
        exp.Supplier_id = data.Supplier_id
        exp.Min_Quantity = data.Min_Quantity
        exp.Article = data.Article
        exp.External_Code = data.External_Code
        exp.Unit_of_Measure = data.Unit_of_Measure
        exp.Description = data.Description
        exp.Cell = data.Cell
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(Products).filter(Products.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
