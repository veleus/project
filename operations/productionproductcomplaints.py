from dto.model import ProductionProductComplaints as model
from tables.database import ProductionProductComplaints
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionProductComplaints).filter(ProductionProductComplaints.ID == id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductComplaints(ID_Product = data.ID_Product, 
                                        User_Name = data.User_Name, 
                                        Date = data.Date, 
                                        Complaint_Text = data.Complaint_Text, 
                                        Status = data.Status, 
                                        Resolution_Text = data.Resolution_Text)
        db.add(exp)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: model):
    try:
        exp = db.query(ProductionProductComplaints).filter(ProductionProductComplaints.ID == data.ID).first()
        exp.ID_Product = data.ID_Product
        exp.User_Name = data.User_Name
        exp.Date = data.Date
        exp.Complaint_Text = data.Complaint_Text
        exp.Status = data.Status
        exp.Resolution_Text = data.Resolution_Text
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()



def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductComplaints).filter(ProductionProductComplaints.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp