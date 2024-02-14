from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, VARCHAR

from database import Base


class ProductGroups(Base):
    __tablename__ = 'ProductGroups'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Parent_ID = Column(Integer, ForeignKey('ProductGroups.ID'))
    Group_Code = Column(String(255))
    Name = Column(String(255))
    Description = Column(String(255))


class Products(Base):
    __tablename__ = 'Products'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Group_ID = Column(Integer, ForeignKey('ProductGroups.ID'))
    Nomenclature = Column(String(255))
    Supplier_id = Column(String(255), ForeignKey('Suppliers.ID'))
    Min_Quantity = Column(Integer)
    Article = Column(String(255))
    External_Code = Column(String(255))
    Unit_of_Measure = Column(VARCHAR(255))
    Description = Column(VARCHAR(255))
    Cell = String(255)

class Warehouse(Base):
    __tablename__ = 'Warehouse'
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Warehouse_ID = Column(Integer, primary_key=True, autoincrement=True)
    Quantity=Column(Integer)
    In_Transit= Column(Integer)
    Reserved = Column(Integer)
    In_Production = Column(Integer)

class Suppliers(Base):
    __tablename__ = 'Suppliers'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Warehouse_ID = Column(Integer, ForeignKey('Warehouse.Warehouse_ID'))
    Name = Column(String(255))
    Phone = Column(String(255))
    Address = Column(String(255))
    Email = Column(String(255))
    INN = Column(String(255))
    Contact_Manager = Column(String(255))
    Delivery_Time = Column(String(255))
    Country = Column(String(255))


class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Full_Name = Column(String(255))
    Phone = Column(String(255))
    Addres = Column(String(255))
    Email = Column(String(255))
    Country = Column(String(255))
    Login = Column(String(255))
    Password = Column(String(255))
    Role_User = Column(Integer, ForeignKey('Role.ID'))

    
class DocumentTypesDDM(Base):
    __tablename__ = 'DocumentTypesDDM'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255))
    Description = Column(String(255))
    Warehouse = Column(Integer)
    Reserve = Column(Integer)
    In_Transit = Column(Integer)
    In_Production = Column(Integer)

class SupplierOrders(Base):
    __tablename__ = 'SupplierOrders'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Supplier = Column(Integer, ForeignKey('Suppliers.ID'))
    Creation_Date = Date
    Order_Number = Column(String(255))
    Status_ID = Column(Integer)
    Paid = Column(Boolean)
    Delivery_Date = Column(Date)


class SupplierOrderItems(Base):
    __tablename__ = 'SupplierOrderItems'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Order = Column(Integer, ForeignKey('SupplierOrders.ID'), primary_key=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'),  primary_key=True)
    Quantity =Column(Integer)

class MaterialMovements(Base):
    __tablename__ = 'MaterialMovements'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Document_Type = Column(Integer, primary_key=True)
    Document_Base_Number  = Column(Integer, primary_key=True)
    Receipt_Date = Column(Date)
    ID_Contractor = Column(Integer, ForeignKey('Suppliers.ID'), primary_key=True)
    ID_Employee = Column(Integer, ForeignKey('User.ID'))

class MaterialMovementItems(Base):
    __tablename__ = 'MaterialMovementItems'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Movement = Column(Integer, ForeignKey('MaterialMovements.ID'), primary_key=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID') ,primary_key=True)
    Quantity  = Column(Integer)
    Comment  = Column(VARCHAR(255))


class TechMap(Base):
    __tablename__ = 'TechMap'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255))
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Comment = Column(String(255))


class Stages(Base):
    __tablename__ = 'Stages'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255))
    Description = Column(String(255))
    ID_TechMap = Column(Integer, ForeignKey('TechMap.Id'))
    Num = Column(Integer)
    Exec_time = Column(Integer)
    Cost = Column(Integer)



class StagesToMaterial(Base):
    __tablename__ = 'StagesToMaterial'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Stages = Column(Integer, ForeignKey('Stages.ID') ,primary_key=True)
    ID_Materials  = Column(Integer, ForeignKey('Materials.ID'),primary_key=True, )
    Quantity = Column(Integer)


class ProductionTask(Base):
    __tablename__ = 'ProductionTask'
    Date = Column(Date, primary_key=True)
    Warehouse_Materials =Column(Integer)
    Warehouse_Products  = Column(Integer)
    ID_TechMap = Column(Integer, ForeignKey('TechMap.Id') ,primary_key=True)
    Quantity = Column(Integer)


class ProdExecution(Base):
    __tablename__ = 'ProdExecution'
    ID = Column(Integer, primary_key=True)
    ID_ProdTask = Column(Date, ForeignKey('ProductionTask.Date'), primary_key=True)
    ID_Stage = Column(Integer ,ForeignKey('Stages.ID'))
    ID_User = Column(Integer, ForeignKey('User.ID'))
    Date_Start = Column(Date)
    Quantity = Column(Integer)
    Date_Finish = Column(Date)

class ReadnisStagesToProduct(Base):
    __tablename__ = 'ReadnisStagesToProduct'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_ProdExec = Column(Integer, ForeignKey('ProdExecution.ID') ,primary_key=True)
    ID_Materials = Column(Integer, ForeignKey('Materials.ID') ,primary_key=True)
    Quantity = Column(Integer)

class ReadnisStagesToMaterial(Base):
    __tablename__ = 'ReadnisStagesToMaterial'
    ID = Column(Integer, primary_key=True)
    ID_ProdExe = Column(Integer, ForeignKey('ProdExecution.ID'))
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Prod_Quantity = Column(Integer)

class ProductionProductItems(Base):
    __tablename__ = 'ProductionProductItems'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_TechMap = Column(Integer, ForeignKey('TechMap.Id') ,primary_key=True)
    ID_Material  = Column(Integer, ForeignKey('Materials.ID') ,primary_key=True)
    Value  = Column(Integer)

class ProductionMaterialItems(Base):
    __tablename__ = 'ProductionMaterialItems'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID') ,primary_key=True)
    Value = Column(Integer)


class ProductionMaterialRequests(Base):
    __tablename__ = 'ProductionMaterialRequests'
    ID = Column(Integer, primary_key=True)
    ID_User = Column(Integer, ForeignKey('User.ID'))
    Date = Column(Date)
    Status  = Column(String(255))
    Description = Column(String(255))


class ProductionMaterialRequestItems(Base):
    __tablename__ = 'ProductionMaterialRequestItems'
    ID = Column(Integer, primary_key=True)
    ID_Request  = Column(Integer, ForeignKey('ProductionMaterialRequests.ID'))
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Quantity = Column(Integer)

class ProductionMaterialTransfers(Base):
    __tablename__ = 'ProductionMaterialTransfers'
    ID  = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    From_Warehouse = Column(Integer)
    To_Warehouse  = Column(Integer)
    Quantity = Column(Integer)
    Date = Column(Date)
    Reason  = Column(String(255))


class ProductionMaterialDefects(Base):
    __tablename__ = 'ProductionMaterialDefects'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Quantity  = Column(Integer)
    Date = Column(Date)
    Reason = Column(String(255))
    Description = Column(String(255))

class ProductionProductDefects(Base):
    __tablename__ = 'ProductionProductDefects'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Quantity = Column(Integer)
    Date  = Column(Date)
    Reason = Column(String(255))
    Description = Column(String(255))

class ProductionMachineLog(Base):
    __tablename__ = 'ProductionMachineLog'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Machine_ID = Column(Integer, ForeignKey('Machines.ID'))
    Date = Column(Date)
    Operation_Performed  = Column(String(255))
    Operator = Column(String(255))
    Status = Column(String(255))

class ProductionQualityControl(Base):
    __tablename__ = 'ProductionQualityControl'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Date = Column(Date)
    Inspector = Column(String(255))
    Status = Column(String(255))
    Comments  = Column(String(255))


class ProductionProductSerialNumbers(Base):
    __tablename__ = 'ProductionProductSerialNumbers'
    ID  = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Serial_Number = Column(String(255))


class ProductionMaterialSerialNumbers(Base):
    __tablename__ = 'ProductionMaterialSerialNumbers'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Serial_Number = Column(String(255))


class ProductionProductAssemblyLog(Base):
    __tablename__ = 'ProductionProductAssemblyLog'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_ProdExec = Column(Integer, ForeignKey('ProdExecution.ID'))
    Assembly_Step = Column(String(255))
    Date = Column(Date)
    Employee = Column(String(255))
    Status = Column(String(255))


class ProductionMaterialUsage(Base):
    __tablename__ = 'ProductionMaterialUsage'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_ProdExec = Column(Integer, ForeignKey('ProdExecution.ID'))
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Quantity_Used  = Column(Integer)
    Date = Column(Date)

class ProductionMaterialSupplierHistory(Base):
    __tablename__ = 'ProductionMaterialSupplierHistory'
    ID  = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    ID_Supplier = Column(Integer, ForeignKey('Suppliers.ID'))
    Date = Column(Date)
    Quantity = Column(Integer)
    Price = Column(Integer)


class ProductionProductSales(Base):
    __tablename__ = 'ProductionProductSales'
    ID  = Column(Integer ,primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Date = Column(Date)
    Quantity = Column(Integer)
    Sale_Price = Column(Integer)



class ProductionProductReturns(Base):
    __tablename__ = 'ProductionProductReturns'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Date = Column(Date)
    Quantity = Column(Integer)
    Return_Reason = Column(String(255))
    Comments =Column(String(255))

class ProductionMaterialCosts(Base):
    __tablename__ = 'ProductionMaterialCosts'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Cost = Column(Integer)
    Date = Column(Date)
    Description = Column(String(255))

class ProductionProductCosts(Base):
    __tablename__ = 'ProductionProductCosts'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Cost = Column(Integer)
    Date = Column(Date)
    Description = Column(String(255))

class ProductionEmployeeAttendance(Base):
    __tablename__ = 'ProductionEmployeeAttendance'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_User = Column(Integer, ForeignKey('User.ID'))
    Date = Column(Date)
    Attendance_Status = Column(String(255))


class Materials(Base):
    __tablename__ = 'Materials'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255))
    Description = Column(String(255))
    Warehouse = Column(Integer, ForeignKey('Warehouse.Warehouse_ID'))

class Machines(Base):
    __tablename__ = 'Machines'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Machine_Name = Column(String(255))
    Description = Column(String(255))


class ProductionProductInventory(Base):
    __tablename__ = 'ProductionProductInventory'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Date = Column(Date)
    Actual_Quantity = Column(Integer)
    Comments = Column(String(255))


class ProductionMaterialInventory(Base):
    __tablename__ = 'ProductionMaterialInventory'
    ID =Column(Integer, primary_key=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Date = Column(Date)
    Actual_Quantity = Column(Integer)
    Comments = Column(String(255))


class ProductionProductPromotions(Base):
    __tablename__ = 'ProductionProductPromotions'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Promotion_Name = Column(String(255))
    Start_Date = Column(Date)
    End_Date = Column(Date)
    Discount_Percentage = Column(Integer)


class ProductionMaterialSuppliers(Base):
    __tablename__ = 'ProductionMaterialSuppliers'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    ID_Supplier = Column(Integer, ForeignKey('Suppliers.ID'))


class ProductionProductCategories(Base):
    __tablename__ = 'ProductionProductCategories'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Category_Name = Column(String(255))

class ProductionMaterialCategories(Base):
    __tablename__ = 'ProductionMaterialCategories'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Material  = Column(Integer, ForeignKey('Materials.ID'))
    Category_Name  = Column(VARCHAR(255))


class ProductionProductReviews(Base):
    __tablename__ = 'ProductionProductReviews'
    ID = Column(Integer,primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    User_Name = Column(String(255))
    Rating = Column(Integer)
    Review_Text  = Column(String(255))
    Date = Column(Date)


class ProductionMaterialSupplierContacts(Base):
    __tablename__ = 'ProductionMaterialSupplierContacts'
    ID  = Column(Integer, primary_key=True, autoincrement=True)
    ID_Supplier = Column(Integer, ForeignKey('Suppliers.ID'))
    Contact_Type  = Column(String(255))
    Contact_Value = Column(String(255))


class ProductionProductSupplierContacts(Base):
    __tablename__ = 'ProductionProductSupplierContacts'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Supplier =  Column(Integer,  ForeignKey('Suppliers.ID'))
    Contact_Type = Column(String(255))
    Contact_Value = Column(String(255))

class ProductionProductAttributes(Base):
    __tablename__ = 'ProductionProductAttributes'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Attribute_Name = Column(String(255))
    Attribute_Value = Column(String(255))

class ProductionMaterialAttributes(Base):
    __tablename__ = 'ProductionMaterialAttributes'
    ID =Column(Integer, primary_key=True, autoincrement=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Attribute_Name = Column(String(255))
    Attribute_Value = Column(String(255))


class ProductionEmployeeSkills(Base):
    __tablename__ = 'ProductionEmployeeSkills'
    ID = Column(Integer,primary_key=True, autoincrement=True)
    ID_User = Column(Integer, ForeignKey('User.ID'))
    Skill_Name = Column(String((255)))
    Skill_Level = Column(String(255))


class ProductionProductWarranty(Base):
    __tablename__ = 'ProductionProductWarranty'
    ID = Column(Integer, primary_key=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Warranty_Period = Column(Integer)
    Warranty_Description = Column(String(255))

class ProductionMaterialAvailability(Base):
    __tablename__ = 'ProductionMaterialAvailability'
    ID = Column(Integer, primary_key=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Warehouse_Availability = Column(Integer)
    In_Transit = Column(Integer)
    Reserved = Column(Integer)

class ProductionWorkOrders(Base):
    __tablename__ = 'ProductionWorkOrders'
    ID = Column(Integer, primary_key=True)
    ID_User = Column(Integer, ForeignKey('User.ID'))
    Date_Assigned = Column(Date)
    Planned_Start_Date = Column(Date)
    Planned_End_Date = Column(Date)
    Status = Column(String(255))
    Actual_Start_Date = Column(Date)
    Actual_End_Date = Column(Date)
    Reason_Cancelled = Column(String(255))


class ProductionDefects(Base):
    __tablename__ = 'ProductionDefects'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrderItem = Column(Integer, ForeignKey('ProductionWorkOrderItems.ID'))
    Quantity  = Column(Integer)
    Date = Column(Date)
    Reason = Column(String(255))
    Description = Column(String(255))


class ProductionMaterialConsumption(Base):
    __tablename__ = 'ProductionMaterialConsumption'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrderItem = Column(Integer, ForeignKey('ProductionWorkOrderItems.ID'))
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Quantity_Used = Column(Integer)
    Date = Column(Date)


class ProductionMaterialSurplus(Base):
    __tablename__ = 'ProductionMaterialSurplus'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrderItem = Column(Integer, ForeignKey('ProductionWorkOrderItems.ID'))
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Quantity_Surplus = Column(Integer)
    Date = Column(Date)
    Reason = Column(String(255))
    Description  = Column(String(255))


class ProductionProductAssemblySteps(Base):
    __tablename__ = 'ProductionProductAssemblySteps'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrderItem = Column(Integer, ForeignKey('ProductionWorkOrderItems.ID'))
    Step_Number = Column(Integer)
    Description  = Column(String(255))
    Estimated_Duration  = Column(Integer) 
    Actual_Start_Date = Column(Date)
    Actual_End_Date = Column(Date)
    Status  = Column(String(255))
    Reason_Cancelled = Column(String(255))

class ProductionWorkOrderStatusHistory(Base):
    __tablename__ = 'ProductionWorkOrderStatusHistory'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrder = Column(Integer, ForeignKey('ProductionWorkOrders.ID'))
    Status = Column(String(255))
    Date_Changed = Column(Date)

class ProductionEmployeeProductivity(Base):
    __tablename__ = 'ProductionEmployeeProductivity'
    ID = Column(Integer, primary_key=True)
    ID_User = Column(Integer, ForeignKey('User.ID'))
    ID_WorkOrderItem = Column(Integer, ForeignKey('ProductionWorkOrderItems.ID'))
    Productivity_Value = Column(Integer)
    Date_Recorded = Column(Date)

class ProductionMachineMaintenance(Base):
    __tablename__ = 'ProductionMachineMaintenance'
    ID = Column(Integer, primary_key=True)
    ID_Machine = Column(Integer, ForeignKey('Machines.ID'))
    Date = Column(Date)
    Maintenance_Type = Column(String(255))
    Description = Column(String(255))
    Cost = Column(Integer)


class  ProductionProductComplaints(Base):
    __tablename__ = 'ProductionProductComplaints'
    ID = Column(Integer, primary_key=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    User_Name = Column(String(255))
    Date = Column(Date)
    Complaint_Text = Column(String(255))
    Status = Column(String(255))
    Resolution_Text = Column(String(255))


class Quantity_Remaining(Base):
    __tablename__ = 'ProductionMaterialExpiration'
    ID = Column(Integer, primary_key=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Date_S = Column(Date)
    Expiration_Date = Column(Date)
    Quantity_Remaining = Column(Integer)

class ProductionProductExpiration(Base):
    __tablename__ = 'ProductionProductExpiration'
    ID = Column(Integer, primary_key=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Expiration_Date = Column(Date)
    Quantity_Remaining = Column(Integer)

class ProductionMaterialForecast(Base):
    __tablename__ = 'ProductionMaterialForecast'
    ID = Column(Integer, primary_key=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Forecast_Date = Column(Date)
    Forecast_Quantity = Column(Integer)

class ProductionProductReturnsReasons(Base):
    __tablename__ = 'ProductionProductReturnsReasons'
    ID = Column(Integer, primary_key=True)
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    Reason_Name = Column(String(255))
    Description = Column(String(255))

class ProductionMaterialReturnsReasons(Base):
    __tablename__ = 'ProductionMaterialReturnsReasons'
    ID = Column(Integer, primary_key=True)
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Reason_Name = Column(String(255))
    Description = Column(String(255))

class ProductionWorkOrderStages(Base):
    __tablename__ = 'ProductionWorkOrderStages'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrderItem = Column(Integer, ForeignKey('ProductionWorkOrders.ID'))
    ID_Stage = Column(Integer, ForeignKey('Stages.ID'))
    Start_Date = Column(Date)
    End_Date = Column(Date)
    Status = Column(String(255))

class ProductionWorkOrderStatus(Base):
    __tablename__ = 'ProductionWorkOrderStatus'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrder = Column(Integer, ForeignKey('ProductionWorkOrders.ID'))
    Status = Column(String(255))

class  ProductionWorkOrderItems(Base):
    __tablename__ = 'ProductionWorkOrderItems'
    ID = Column(Integer, primary_key=True)
    ID_WorkOrder = Column(Integer, ForeignKey('ProductionWorkOrders.ID'))
    ID_Product = Column(Integer, ForeignKey('Products.ID'))
    ID_Material = Column(Integer, ForeignKey('Materials.ID'))
    Planned_Quantity = Column(Integer)
    Actual_Quantity = Column(Integer)
    Status = Column(String(255))
    Reason_Cancelled = Column(String(255))


class Role(Base):
    __tablename__ = 'Role'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Role = Column(String(255))  # Add index=True to create an index on this column
    