from dto.model import ReadnisStagesToProduct as model
from sqlalchemy.exc import SQLAlchemyError
from tables.database import ReadnisStagesToProduct
from sqlalchemy.orm import Session

def get_task(db: Session, user_id:int):
    return db.query(ReadnisStagesToProduct).filter(ReadnisStagesToProduct.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ReadnisStagesToProduct(ID_ProdExec = data.ID_ProdExec, 
                                    ID_Materials = data.ID_Materials, 
                                    Quantity = data.Quantity)
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
        exp = db.query(ReadnisStagesToProduct).filter(ReadnisStagesToProduct.ID == id).first()
        exp.ID_ProdExec = data.ID_ProdExec
        exp.ID_Materials = data.ID_Materials
        exp.Quantity = data.Quantity
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
        


def delete_task(db: Session, id: int):
    exp = db.query(ReadnisStagesToProduct).filter(ReadnisStagesToProduct.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp


