from tables.database import DocumentTypesDDM as DocumentTypes
from dto.model import DocumentTypesDDM
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


def get_task(db: Session, user_id:int):
    return db.query(DocumentTypes).filter(DocumentTypes.ID == user_id).first()

def create_task(db: Session, data: DocumentTypesDDM):
    try:
        exp = DocumentTypes(Name = data.Name, Description = data.Description, Warehouse = data.Warehouse, Reserve = data.Reserve, In_Transit = data.In_Transit, In_Production = data.In_Production)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()
def update_task(db: Session, data: DocumentTypesDDM):
    try:
        exp = db.query(DocumentTypes).filter(DocumentTypes.ID == data.ID).first()
        exp.Name = data.Name
        exp.Description = data.Description
        exp.Warehouse = data.Warehouse
        exp.Reserve = data.Reserve
        exp.In_Transit = data.In_Transit
        exp.In_Production = data.In_Production
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(DocumentTypes).filter(DocumentTypes.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp