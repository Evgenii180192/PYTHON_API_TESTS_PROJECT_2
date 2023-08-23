from loguru import logger
from pydantic import BaseModel, field_validator
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ItemsPerson(BaseModel):
    u_age: int
    u_name: list
    u_salary_5_years: float

    @field_validator("u_age")
    @classmethod
    def check_value_u_age_object_info_2(cls, value_u_age):
        logger.info("Check value u_age object_info_2")
        if value_u_age != PAYLOAD_TOTAL.get("age"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("u_salary_5_years")
    @classmethod
    def check_value_u_salary_5_years(cls, value_salary):
        logger.info("Check value u_salary_5_years object_info_2")
        if value_salary != (PAYLOAD_TOTAL.get("salary") * 4.2):
            raise ValueError(ValueResponseError.Error.value)
