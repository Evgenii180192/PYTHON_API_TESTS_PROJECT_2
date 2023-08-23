from loguru import logger
from pydantic import BaseModel, field_validator
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ModelItemsFamily(BaseModel):
    children: list
    u_salary_1_5_year: int

    @field_validator("u_salary_1_5_year")
    @classmethod
    def check_value_u_salary_1_5_year_get_test_user(cls, value_salary):
        logger.info("Check value u_salary_1_5_year get_test_user")
        if value_salary != PAYLOAD_TOTAL.get("salary") * 4:
            raise ValueError(ValueResponseError.Error.value)
