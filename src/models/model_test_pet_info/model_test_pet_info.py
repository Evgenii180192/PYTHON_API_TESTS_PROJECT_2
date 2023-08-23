from loguru import logger
from pydantic import BaseModel, field_validator
from src.configuration import PAYLOAD_TEST_PET_INFO
from src.errors import ValueResponseError


class ModelTestPetInfo(BaseModel):
    age: int
    daily_food: float
    daily_sleep: float
    name: str

    @field_validator("age")
    @classmethod
    def check_value_age_test_pet_info(cls, value_age):
        logger.info("Check value age test_pet_info")
        if value_age != PAYLOAD_TEST_PET_INFO.get("age"):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("daily_food")
    @classmethod
    def check_value_daily_food_test_pet_info(cls, value_daily_food):
        logger.info("Check value daily_food test_pet_info")
        if value_daily_food != PAYLOAD_TEST_PET_INFO.get("weight") * 0.012:
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("daily_sleep")
    @classmethod
    def check_value_daily_sleep_test_pet_info(cls, value_daily_sleep):
        logger.info("Check value daily_sleep test_pet_info")
        if value_daily_sleep != PAYLOAD_TEST_PET_INFO.get("weight") * 2.5:
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("name")
    @classmethod
    def check_value_name_test_pet_info(cls, value_name):
        logger.info("Check value name test_pet_info")
        if value_name != PAYLOAD_TEST_PET_INFO.get("name"):
            raise ValueError(ValueResponseError.Error.value)


json_schema_test_pet_info = ModelTestPetInfo.model_json_schema()