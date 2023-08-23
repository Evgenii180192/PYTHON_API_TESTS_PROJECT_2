from loguru import logger
from pydantic import BaseModel, field_validator
from src.models.model_user_info_3.model_family_user_info_3 import ModelItemsFamily
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ModelUserInfo3(BaseModel):
    age: str
    family: ModelItemsFamily
    name: str
    salary: int

    @field_validator("age")
    @classmethod
    def check_value_age_user_info_3(cls, value_age):
        logger.info("Check value age user_info_3")
        if int(value_age) != PAYLOAD_TOTAL.get("age"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator('name')
    @classmethod
    def check_value_name_user_info_3(cls, value_name):
        logger.info("Check value name user_info_3")
        if len(value_name) < 2 or value_name != PAYLOAD_TOTAL.get("name"):
            raise ValueError(ValueResponseError.Error.value)


    @field_validator("salary")
    @classmethod
    def check_value_salary_user_info_3(cls, value_salary):
        logger.info("Check value salary user_info_3")
        if value_salary != PAYLOAD_TOTAL.get("salary"):
            raise ValueError(ValueResponseError.Error.value)


# Getting JSON Schema
json_schema_user_info_3 = ModelUserInfo3.model_json_schema()
