from dto.model import ProductionProductReviews as model
from sqlalchemy.orm import Session
from tables.database import ProductionProductReviews
from sqlalchemy.exc import SQLAlchemyError
def get_task(db: Session, user_id:int):
    return db.query(ProductionProductReviews).filter(ProductionProductReviews.ID == user_id).first()

def create_task(db: Session, data: model):
    try:
        exp = ProductionProductReviews(ID_Product = data.ID_Product, 
                                    User_Name = data.User_Name, 
                                    Rating = data.Rating, 
                                    Review_Text = data.Review_Text,
                                    Date = data.Date)
        db.add(exp)
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def update_task(db: Session, data: model, id):
    exp = db.query(ProductionProductReviews).filter(ProductionProductReviews.ID == id).first()
    exp.ID_Product = data.ID_Product
    exp.User_Name = data.User_Name
    exp.Rating = data.Rating
    exp.Review_Text = data.Review_Text
    exp.Date = data.Date
    db.commit()
    return exp

def delete_task(db: Session, id: int):
    exp = db.query(ProductionProductReviews).filter(ProductionProductReviews.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp
