from pydantic import BaseModel
from datetime import date



class ProductGroups(BaseModel):
    
    Parent_ID: int
    Group_Code: str
    Name: str
    Description: str

class Products(BaseModel):
    Group_ID: int
    Nomenclature : str
    Supplier_id: str
    Min_Quantity: int
    Article: str
    External_Code: str
    Unit_of_Measure: str
    Description: str
    Cell: str

class Warehouse(BaseModel):
    ID_Product: int
    Quantity : int
    In_Transit : int
    Reserved : int
    In_Production : int

class Suppliers(BaseModel):
    
    Warehouse_ID: int
    Name: str
    Phone: str
    Address: str
    Email: str
    INN: str
    Contact_Manager: str
    Delivery_Time: str
    Country: str

class Employee(BaseModel):
    
    Full_Name: str
    Phone: str
    Address: str
    Email: str
    County: str
    Login: str
    Password: str
    Role: int
class ReadnisStagesToMaterial(BaseModel):
    ID_ProdExe: int
    ID_Material: int
    Prod_Quantity: int

class Role(BaseModel):
    role: str

class DocumentTypesDDM(BaseModel):
    
    Name: str
    Description: str
    Warehouse: int
    Reserve: int
    In_Transit : int
    In_Production : int

class SupplierOrders(BaseModel):
    
    ID_Supplier: int
    Creation_Date: date
    Order_Number: str
    Status_ID : int
    Paid : bool
    Delivery_Date: date

class SupplierOrderItems(BaseModel):
    ID_Order: int
    ID_Product: int
    Quantity: int

class MaterialMovements(BaseModel):
    
    Document_Type : int
    Document_Base_Number : int
    Receipt_Date : date
    ID_Contractor : int
    ID_Employee : int

class MaterialMovementItems(BaseModel):
    ID_Movement : int
    ID_Product : int
    Quantity : int
    Comment: str

class TechMap(BaseModel):
    
    Name: str
    ID_Material : int
    Comment : str


class Stages(BaseModel):
    
    Name: str
    Description: str
    ID_TechMap : int
    Num : int
    Exec_time: int
    Cost : int

class StagesToMaterial(BaseModel):
    ID_Stages : int
    ID_Material : int
    Quantity : int


class ProductionTask(BaseModel):
    Date: date
    Warehouse_Materials : int
    Warehouse_Products : int 
    ID_TechMap : int
    Quantity : int

class ProdExecution(BaseModel):
    
    ID_ProdTask : int
    ID_Stage : int
    ID_User : int
    Date_Start : date
    Quantity : int 
    Date_Finish : date


class ReadnisStagesToProduct(BaseModel):
    
    ID_ProdExec : int
    ID_Materials : int
    Quantity : int


class ProductionProductItems(BaseModel):
    
    ID_TechMap : int
    ID_Material : int
    Value : int
    

class ProductionMaterialItems(BaseModel):
    
    ID_Material : int
    Value : int

class ProductionMaterialRequests(BaseModel):
    
    ID_User : int
    Date: date
    Status : str
    Description : str

class ProductionMaterialRequestItems(BaseModel):
    
    ID_Request : int
    ID_Material : int
    Quantity : int

class ProductionMaterialTransfers(BaseModel):
    
    ID_Material : int
    From_Warehouse : int
    To_Warehouse : int
    Quantity : int
    Date : date
    Reason : str


class ProductionMaterialDefects(BaseModel):
    
    ID_Material : int
    Quantity : int
    Date : date
    Reason : str
    Description : str

class ProductionProductDefects(BaseModel):
    
    ID_Product : int
    Quantity : int
    Date : date
    Reason : str
    Description : str

class ProductionMachineLog(BaseModel):
    
    Machine_ID : int
    Date : date
    Operation_Performed : str
    Operator : str
    Status : str

class ProductionQualityControl(BaseModel):
    
    ID_Product : int
    Date: date
    Inspector : str
    Status : str
    Comments : str


class ProductionProductSerialNumbers(BaseModel):
    
    ID_Product : int
    Serial_Number : str


class ProductionMaterialSerialNumbers(BaseModel):
    
    ID_Material : int
    Serial_Number : str

class ProductionProductAssemblyLog(BaseModel):
    
    ID_ProdExec : int
    Assembly_Step : str
    Date : date
    Employee : str
    Status : str

class ProductionMaterialUsage(BaseModel):
    
    ID_ProdExec : int
    ID_Material: int
    Quantity_Used : int
    Date : date


class ProductionMaterialSupplierHistory(BaseModel):
    
    ID_Material : int
    ID_Supplier : int
    Date : date
    Quantity : int
    Price : int

class ProductionProductSales(BaseModel):
    
    ID_Product : int
    Date : date
    Quantity : int
    Sale_Price : int


class ProductionProductReturns(BaseModel):
    
    ID_Product : int
    Date : date
    Quantity : int
    Return_Reason : str
    Comments : str

class ProductionMaterialCosts(BaseModel):
    
    ID_Material : int
    Cost : int
    Date : date
    Description : str


class ProductionProductCosts(BaseModel):
    
    ID_Product: int
    Cost : int
    Date : date
    Description : str


class ProductionEmployeeAttendance(BaseModel):
    
    ID_User : int
    Date : date
    Attendance_Status : str

class Materials(BaseModel):
     
    Name: str
    Description: str


class Machines(BaseModel):
    
    Machine_Name: str
    Description: str

class ProductionProductInventory(BaseModel):
    
    ID_Product : int
    Date: date
    Actual_Quantity : int
    Comments : str


class ProductionMaterialInventory(BaseModel):
    
    ID_Material : int
    Date: date
    Actual_Quantity : int
    Comments : str

class ProductionProductPromotions(BaseModel):
    
    ID_Product : int
    Promotion_Name : str
    Start_Date : date
    End_Date : date
    Discount_Percentage : int


class ProductionMaterialSuppliers(BaseModel):
    
    ID_Material : int
    ID_Supplier : int


class ProductionProductCategories(BaseModel):
    
    ID_Product : int
    Category_Name : str

class ProductionMaterialCategories(BaseModel):
    
    ID_Material : int
    Category_Name : str


class ProductionProductReviews(BaseModel):
    
    ID_Product : int
    User_Name : str
    Rating : int
    Review_Text : str
    Date : date

class ProductionMaterialSupplierContacts(BaseModel):
    
    ID_Supplier : int
    Contact_Type: str
    Contact_Value : str

class ProductionProductSupplierContacts(BaseModel):
    
    ID_Supplier : int
    Contact_Type: str
    Contact_Value : str


class ProductionProductAttributes(BaseModel):
    
    ID_Product : int
    Attribute_Name : str
    Attribute_Value : str

class ProductionMaterialAttributes(BaseModel):
    
    ID_Material : int
    Attribute_Name : str
    Attribute_Value : str

class ProductionEmployeeSkills(BaseModel):
    
    ID_User : int
    Skill_Name : str
    Skill_Level : str

class ProductionProductWarranty(BaseModel):
    
    ID_Product : int
    Warranty_Period : int
    Warranty_Description : str

class ProductionMaterialAvailability(BaseModel):
    
    ID_Material : int
    Warehouse_Availability : int
    In_Transit : int
    Reserved : int

class ProductionWorkOrders(BaseModel):
    ID_User : int
    Date_Assigned : date
    Planned_Start_Date : date
    Planned_End_Date : date
    Status : str
    Actual_Start_Date : date
    Actual_End_Date : date
    Reason_Cancelled : str



class ProductionDefects(BaseModel):
    
    ID_WorkOrderItem : int
    Quantity : int
    Date : date
    Reason : str
    Description : str


class ProductionMaterialConsumption(BaseModel):
    
    ID_WorkOrderItem : int
    ID_Material : int
    Quantity_Used : int
    Date : date


class ProductionMaterialSurplus(BaseModel):
    
    ID_WorkOrderItem : int
    ID_Material : int
    Quantity_Surplus : int
    Date : date
    Reason : str
    Description : str


class ProductionProductAssemblySteps(BaseModel):
    
    ID_WorkOrderItem : int
    Step_Number : int
    Description  : str
    Estimated_Duration  : int
    Actual_Start_Date  : date
    Actual_End_Date  : date
    Status  : str
    Reason_Cancelled  : str


class ProductionWorkOrderStatusHistory(BaseModel):
    
    ID_WorkOrder : int
    Status : str
    Date : date

class ProductionEmployeeProductivity(BaseModel):
    
    ID_User : int
    ID_WorkOrderItem : int
    Productivity_Value : int
    Date_Recorded : date


class ProductionMachineMaintenance(BaseModel):
    
    ID_Machine : int
    Date : date
    Maintenance_Type : str
    Description : str
    Cost : int


class ProductionProductComplaints(BaseModel):
    
    ID_Product : int
    User_Name : str
    Date : date
    Complaint_Text : str
    Status : str
    Resolution_Text : str



class ProductionMaterialExpiration(BaseModel):
    
    ID_Material : int
    Date_S : date
    Expiration_Date : date
    Quantity_Remaining : int

class ProductionProductExpiration(BaseModel):
    
    ID_Product : int
    Expiration_Date : date
    Quantity_Remaining : int

class ProductionMaterialForecast(BaseModel):
    
    ID_Material : int
    Forecast_Date: date
    Forecast_Quantity : int

class ProductionProductReturnsReasons(BaseModel):
    
    ID_Product : int
    Reason_Name : str
    Description : str

class ProductionMaterialReturnsReasons(BaseModel):
    
    ID_Material : int
    Reason_Name : str
    Description : str

class ProductionWorkOrderStages(BaseModel):
    
    ID_WorkOrderItem : int
    ID_Stage : int
    Start_Date : date
    End_Date : date
    Status : str


class ProductionWorkOrderStatus(BaseModel):
    
    ID_WorkOrder : int
    Status : str

class ProductionWorkOrderItems(BaseModel):
    
    ID_WorkOrder : int
    ID_Product : int
    ID_Material : int
    Planned_Quantity : int
    Actual_Quantity : int
    Status : str
    Reason_Cancelled : str




