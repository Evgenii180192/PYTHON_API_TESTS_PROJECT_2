from loguru import logger
from pydantic import BaseModel, field_validator

from src.models.model_user_info.model_items_person import ModelItemsPerson
from src.configuration import PAYLOAD_USER_INFO
from src.errors import ValueResponseError


class ModelUserInfo(BaseModel):
    person: ModelItemsPerson
    qa_salary_after_12_months: float
    qa_salary_after_6_months: int
    start_qa_salary: int

    @field_validator("qa_salary_after_12_months")
    @classmethod
    def check_value_qa_salary_after_12_months_user_info(cls, value_salary):
        logger.info("Check value qa_salary_after_12_months user_info")
        if value_salary != PAYLOAD_USER_INFO.get("salary") * 2.9:
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("qa_salary_after_6_months")
    @classmethod
    def check_value_qa_salary_after_6_months_user_info(cls, value_salary):
        logger.info("Check value qa_salary_after_6_months user_info")
        if value_salary != (PAYLOAD_USER_INFO.get("salary") * 2):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("start_qa_salary")
    @classmethod
    def check_value_start_qa_salary_user_info(cls, value_salary):
        logger.info("Check value start_qa_salary user_info")
        if value_salary != PAYLOAD_USER_INFO.get("salary"):
            raise ValueError(ValueResponseError.Error.value)


# Getting json schema
json_schema_user_info = ModelUserInfo.model_json_schema()
