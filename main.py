from fastapi import FastAPI
import uvicorn
from database import engine
from tables.database import Base

Base.metadata.create_all(bind=engine)

from routers import (
    documentTypesDDM, employees, materialMovementItems, materialMovements, prodExecution, 
    productgroups, productionDefects, productionEmployeeAttendance, 
    ProductionEmployeeProductivity, productionEmployeeSkills, productionMachineLog, 
    productionMachineMaintenance, productionMaterialAvailability, productionMaterialCategories, 
    productionMaterialConsumption, productionMaterialCosts, productionMaterialDefects, productionMaterialForecast, productionMaterialInventory, 
    productionMaterialRequestItems, productionMaterialRequests, productionMaterialReturnsReasons, 
    productionMaterialSerialNumbers, productionMaterialSupplierContacts, productionMaterialSupplierHistory, 
    productionMaterialSuppliers, productionMaterialSurplus, productionMaterialUsage, 
    productionProductAssemblyLog, productionProductAssemblySteps, productionProductAttributes, 
    productionProductCategories, productionProductComplaints, productionProductCosts, 
    productionProductDefects, productionProductExpiration, 
    productionProductInventory, productionProductItems, productionProductPromotions, 
    productionProductReturns, productionProductReturnsReasons, productionProductReviews, 
    productionProductSales, productionProductSerialNumbers, productionProductSupplierContacts, productionProductWarranty, productionQualityControl, 
    productionTask, productionWorkOrderItems, productionWorkOrders, productionWorkOrderStages, 
    productionWorkOrderStatus, productionWorkOrderStatusHistory, products, readnisStagesToMaterial, 
    readnisStagesToProduct, stages, stagesToMaterial, supplierOrderItems, 
    supplierOrders, suppliers, techMap, warehouse, productionMaterialItems, productionMaterialTransfers, materials, products, machines, role
)
# ProductionMaterialTransfers, Materials, Machines, ProductionMaterialAttributes, Quantity_Remaining
app = FastAPI()

app.include_router(documentTypesDDM.router, tags=['documentTypesDDM'])
app.include_router(employees.router, tags=['user'])
app.include_router(materialMovementItems.router, tags=['materialMovementItems'])
app.include_router(materialMovements.router, tags=['materialMovements'])
app.include_router(prodExecution.router, tags=['prodExecution'])
app.include_router(productgroups.router, tags=['productgroups'])
app.include_router(productionDefects.router, tags=['productionDefects'])
app.include_router(productionEmployeeAttendance.router, tags=['productionEmployeeAttendance'])
app.include_router(ProductionEmployeeProductivity.router, tags=['ProductionEmployeeProductivity'])
app.include_router(productionEmployeeSkills.router, tags=['productionEmployeeSkills'])
app.include_router(productionMachineLog.router, tags=['productionMachineLog'])
app.include_router(productionMachineMaintenance.router, tags=['productionMachineMaintenance'])
app.include_router(productionMaterialAvailability.router, tags=['productionMaterialAvailability'])
app.include_router(productionMaterialCategories.router, tags=['productionMaterialCategories'])
app.include_router(productionMaterialConsumption.router, tags=['productionMaterialConsumption'])
app.include_router(productionMaterialCosts.router, tags=['productionMaterialCosts'])
app.include_router(productionMaterialDefects.router, tags=['productionMaterialDefects'])
app.include_router(productionMaterialForecast.router, tags=['productionMaterialForecast'])
app.include_router(productionMaterialInventory.router, tags=['productionMaterialInventory'])
app.include_router(productionMaterialRequestItems.router, tags=['productionMaterialRequestItems'])
app.include_router(productionMaterialRequests.router, tags=['productionMaterialRequests'])
app.include_router(productionMaterialReturnsReasons.router, tags=['productionMaterialReturnsReasons'])
app.include_router(productionMaterialSerialNumbers.router, tags=['productionMaterialSerialNumbers'])
app.include_router(productionMaterialSupplierContacts.router, tags=['productionMaterialSupplierContacts'])
app.include_router(productionMaterialSupplierHistory.router, tags=['productionMaterialSupplierHistory'])
app.include_router(productionMaterialSuppliers.router, tags=['productionMaterialSuppliers'])
app.include_router(productionMaterialSurplus.router, tags=['productionMaterialSurplus'])
app.include_router(productionMaterialUsage.router, tags=['productionMaterialUsage'])
app.include_router(productionProductAssemblyLog.router, tags=['productionProductAssemblyLog'])
app.include_router(productionProductAssemblySteps.router, tags=['productionProductAssemblySteps'])
app.include_router(productionProductAttributes.router, tags=['productionProductAttributes'])
app.include_router(productionProductCategories.router, tags=['productionProductCategories'])
app.include_router(productionProductComplaints.router, tags=['productionProductComplaints'])
app.include_router(productionProductCosts.router, tags=['productionProductCosts'])
app.include_router(productionProductDefects.router, tags=['productionProductDefects'])
app.include_router(productionProductExpiration.router, tags=['productionProductExpiration'])
app.include_router(productionProductInventory.router, tags=['productionProductInventory'])
app.include_router(productionProductPromotions.router, tags=['productionProductPromotions'])
app.include_router(productionProductReturns.router, tags=['productionProductReturns'])
app.include_router(productionProductReturnsReasons.router, tags=['productionProductReturnsReasons'])
app.include_router(productionProductReviews.router, tags=['productionProductReviews'])
app.include_router(productionProductSales.router, tags=['productionProductSales'])
app.include_router(productionProductSerialNumbers.router, tags=['productionProductSerialNumbers'])
app.include_router(productionProductSupplierContacts.router, tags=['productionProductSupplierContacts'])
app.include_router(productionProductWarranty.router, tags=['productionProductWarranty'])
app.include_router(productionQualityControl.router, tags=['productionQualityControl'])
app.include_router(productionTask.router, tags=['productionTask'])
app.include_router(productionWorkOrderItems.router, tags=['productionWorkOrderItems'])
app.include_router(productionWorkOrders.router, tags=['productionWorkOrders'])
app.include_router(productionWorkOrderStages.router, tags=['productionWorkOrderStages'])
app.include_router(productionWorkOrderStatus.router, tags=['productionWorkOrderStatus'])
app.include_router(productionWorkOrderStatusHistory.router, tags=['productionWorkOrderStatusHistory'])
app.include_router(products.router, tags=['products'])
app.include_router(readnisStagesToMaterial.router, tags=['readnisStagesToMaterial'])
app.include_router(readnisStagesToProduct.router, tags=['readnisStagesToProduct'])
app.include_router(stages.router, tags=['stages'])
app.include_router(stagesToMaterial.router, tags=['stagesToMaterial'])
app.include_router(supplierOrderItems.router, tags=['supplierOrderItems'])
app.include_router(supplierOrders.router, tags=['supplierOrders'])
app.include_router(suppliers.router, tags=['suppliers'])
app.include_router(techMap.router, tags=['techMap'])
app.include_router(warehouse.router, tags=['warehouse'])
app.include_router(productionProductItems.router, tags=['productionProductItems'])
app.include_router(productionMaterialItems.router, tags=['productionMaterialItems'])
app.include_router(productionMaterialTransfers.router, tags=['productionMaterialTransfers'])

app.include_router(materials.router, tags=['materials'])

app.include_router(machines.router, tags=['machines'])
app.include_router(role.router, tags=['role'])
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)