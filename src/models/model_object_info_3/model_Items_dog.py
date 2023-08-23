from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ValueResponseError


class ItemsDog(BaseModel):
    age: int
    name: str

    @field_validator("age")
    @classmethod
    def check_value_age_dog_object_info_3(cls, value_age):
        logger.info("Check value age dog object_info_3")
        if value_age != 4:
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("name")
    @classmethod
    def check_value_name_dog_object_info_3(cls, value_name):
        logger.info("Check value name dog object_info_3")
        if value_name != "Luky":
            raise ValueError(ValueResponseError.Error.value)
