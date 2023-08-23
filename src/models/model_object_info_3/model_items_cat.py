from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ValueResponseError


class ItemsCat(BaseModel):
    age: int
    name: str

    @field_validator("age")
    @classmethod
    def check_value_age_cat_object_info_3(cls, value_age):
        logger.info("Check value age cat object_info_3")
        if value_age != 3:
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("name")
    @classmethod
    def check_value_name_cat_object_info_3(cls, value_name):
        logger.info("Check value name cat object_info_3")
        if value_name != "Sunny":
            raise ValueError(ValueResponseError.Error.value)
