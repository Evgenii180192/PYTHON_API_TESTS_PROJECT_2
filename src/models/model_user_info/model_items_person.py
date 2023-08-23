from loguru import logger
from pydantic import BaseModel, field_validator
from src.configuration import PAYLOAD_USER_INFO
from src.errors import ValueResponseError


class ModelItemsPerson(BaseModel):
    u_age: int
    u_name: list
    u_salary_1_5_year: int

    @field_validator("u_age")
    @classmethod
    def check_value_u_age_user_info(cls, value_u_age):
        logger.info("Check value u_age user_info")
        if value_u_age != PAYLOAD_USER_INFO.get("age"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("u_salary_1_5_year")
    @classmethod
    def check_value_u_salary_1_5_year_user_info(cls, value_salary):
        logger.info("Check value u_salary_1_5_year user_info")
        if value_salary != (PAYLOAD_USER_INFO.get("salary") * 4):
            raise ValueError(ValueResponseError.Error.value)
