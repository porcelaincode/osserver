from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.crud.device import (
    add_device,
    delete_device,
    retrieve_device,
    retrieve_devices,
    update_device,
)
from src.models.device import (
    UpdateDeviceModel,
    DeviceModel,
)

from src.db import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.post("/", response_description="Device data added into the database")
async def add_device_data(device: DeviceModel = Body(...)):
    device = jsonable_encoder(device)
    new_device = await add_device(device)
    return ResponseModel(new_device, "Device added successfully.")

@router.get("/", response_description="Devices retrieved")
async def get_devices():
    devices = await retrieve_devices()
    if devices:
        return ResponseModel(devices, "Devices data retrieved successfully")
    return ResponseModel(devices, "Empty list returned")


@router.get("/{id}", response_description="Device data retrieved")
async def get_device_data(id):
    device = await retrieve_device(id)
    if device:
        return ResponseModel(device, "Device data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Device doesn't exist.")

@router.put("/{id}")
async def update_device_data(id: str, req: UpdateDeviceModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_device = await update_device(id, req)
    if updated_device:
        return ResponseModel(
            "Device with ID: {} name update is successful".format(id),
            "Device name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the device data.",
    )

@router.delete("/{id}", response_description="Device data deleted from the database")
async def delete_device_data(id: str):
    deleted_device = await delete_device(id)
    if deleted_device:
        return ResponseModel(
            "Device with ID: {} removed".format(id), "Device deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Device with id {0} doesn't exist".format(id)
    )