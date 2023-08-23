from loguru import logger
from pydantic import BaseModel, field_validator

from src.models.model_object_info_3.model_items_pets import ItemsPets
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ItemsFamily(BaseModel):
    children: list
    pets: ItemsPets
    u_salary_1_5_year: int

    @field_validator("u_salary_1_5_year")
    @classmethod
    def check_value_u_salary_1_5_year_object_info_3(cls, value_salary):
        logger.info("Check value u_salary_1_5_year object_info_3")
        if value_salary != (PAYLOAD_TOTAL.get("salary") * 4):
            raise ValueError(ValueResponseError.Error.value)
