from loguru import logger
from pydantic import BaseModel, field_validator
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ModelObjectInfo4(BaseModel):
    age: int
    name: str
    salary: list

    @field_validator("age")
    @classmethod
    def check_value_age_object_info_4(cls, value_age):
        logger.info("Check value age object_info_4")
        if value_age != PAYLOAD_TOTAL.get("age"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("name")
    @classmethod
    def check_value_name_object_info_4(cls, value_name):
        logger.info("Check value name object_info_4")
        if value_name != PAYLOAD_TOTAL.get("name") and len(value_name) < 2:
            raise ValueError(ValueResponseError.Error.value)


    @field_validator("salary")
    @classmethod
    def check_value_first_item_salary_object_info_4(cls, value_salary):
        logger.info("Check value first item salary object_info_4")
        if value_salary[0] != PAYLOAD_TOTAL.get("salary"):
            raise ValueError(ValueResponseError.Error.value)
        if int(value_salary[1]) != (PAYLOAD_TOTAL.get("salary") * 2):
            raise ValueError(ValueResponseError.Error.value)
        if int(value_salary[2]) != (PAYLOAD_TOTAL.get("salary") * 3):
            raise ValueError(ValueResponseError.Error.value)
        assert value_salary[0] < int(value_salary[2]) > int(value_salary[1])


json_schema_object_info_4 = ModelObjectInfo4.model_json_schema()