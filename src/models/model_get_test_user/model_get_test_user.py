from loguru import logger
from pydantic import BaseModel, field_validator

from src.models.model_get_test_user.model_items_family import ModelItemsFamily
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ModelGetTestUser(BaseModel):
    age: str
    family: ModelItemsFamily
    name: str
    salary: int

    @field_validator("age")
    @classmethod
    def check_value_age_get_test_user(cls, value_age):
        logger.info("Check value age get_test_user")
        if int(value_age) != PAYLOAD_TOTAL.get("age"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("name")
    @classmethod
    def check_value_name_get_test_user(cls, value_name):
        logger.info("Check value name get_test_user")
        if value_name != PAYLOAD_TOTAL.get("name"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("salary")
    @classmethod
    def check_value_salary_get_test_user(cls, value_salary):
        logger.info("Check value salary get_test_user")
        if value_salary != PAYLOAD_TOTAL.get("salary"):
            raise ValueError(ValueResponseError.Error.value)

# Getting json schema
json_schema_get_test_user = ModelGetTestUser.model_json_schema()
