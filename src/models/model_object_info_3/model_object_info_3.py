from loguru import logger
from pydantic import BaseModel, field_validator

from src.models.model_object_info_3.model_items_family import ItemsFamily
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ModelObjectInfo3(BaseModel):
    age: str
    family: ItemsFamily
    name: str
    salary: int

    @field_validator("age")
    @classmethod
    def check_value_age_object_info_3(cls, value_age):
        logger.info("Check value age object_info_3")
        if int(value_age) != PAYLOAD_TOTAL.get("age"):
            raise ValueError(ValueResponseError)

    @field_validator("name")
    @classmethod
    def check_value_name_object_info_3(cls, value_name):
        logger.info("Check value name object_info_3")
        if value_name != PAYLOAD_TOTAL.get("name"):
            raise ValueError(ValueResponseError)

    @field_validator("salary")
    @classmethod
    def check_value_salary_object_info_3(cls, value_salary):
        logger.info("Check value name object_info_3")
        if value_salary != PAYLOAD_TOTAL.get("salary"):
            raise ValueError(ValueResponseError)


# Getting json schema
json_schema_object_info_3 = ModelObjectInfo3.model_json_schema()
