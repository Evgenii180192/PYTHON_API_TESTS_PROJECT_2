from loguru import logger
from pydantic import BaseModel, field_validator
from src.configuration import PAYLOAD_OBJECT_INFO_1
from src.errors import ValueResponseError


class ModelObjectInfo1(BaseModel):
    age: int
    daily_food: float
    daily_sleep: float
    name: str

    @field_validator("age")
    @classmethod
    def check_value_age_object_info_1(cls, value_age):
        logger.info("Check value age object_info_1")
        if value_age != PAYLOAD_OBJECT_INFO_1.get("age"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("daily_food")
    @classmethod
    def check_value_daily_food_object_info_1(cls, value_daily_food):
        logger.info("Check value daily_food object_info_1")
        if value_daily_food != (PAYLOAD_OBJECT_INFO_1.get("weight") * 0.012):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("daily_sleep")
    @classmethod
    def check_value_daily_sleep_object_info_1(cls, value_daily_sleep):
        logger.info("Check value daily_sleep object_info_1")
        if value_daily_sleep != (PAYLOAD_OBJECT_INFO_1.get("weight") * 2.5):
            raise ValueError(ValueResponseError.Error.value)


    @field_validator("name")
    @classmethod
    def check_value_name_object_info_1(cls, value_name):
        logger.info("Check value name object_info_1")
        if value_name != PAYLOAD_OBJECT_INFO_1.get("name") or len(value_name) < 2:
            raise ValueError(ValueResponseError.Error.value)


# Getting json schema
json_schema_object_info_1 = ModelObjectInfo1.model_json_schema()