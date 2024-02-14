from dto.model import ProductionMaterialForecast as Model
from tables.database import ProductionMaterialForecast
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_task(db: Session, id: int):
    return db.query(ProductionMaterialForecast).filter(ProductionMaterialForecast.ID == id).first()

def create_task(db: Session, data: Model):
    try:
        exp = ProductionMaterialForecast(ID_Material = data.ID_Material, 
                                        Forecast_Date = data.Forecast_Date, 
                                        Forecast_Quantity = data.Forecast_Quantity)
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
        exp = db.query(ProductionMaterialForecast).filter(ProductionMaterialForecast.ID == id).first()
        exp.ID_Material = data.ID_Material
        exp.Forecast_Date = data.Forecast_Date
        exp.Forecast_Quantity = data.Forecast_Quantity
        db.commit()
        db.refresh(exp)
        return exp
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

def delete_task(db: Session, id: int):
    exp = db.query(ProductionMaterialForecast).filter(ProductionMaterialForecast.ID == id).first()
    db.delete(exp)
    db.commit()
    return exp

