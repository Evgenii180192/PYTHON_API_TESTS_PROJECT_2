from loguru import logger
from pydantic import BaseModel, Field, field_validator
from src.models.model_object_info_2.model_person_object_info_2 import ItemsPerson
from src.configuration import PAYLOAD_TOTAL
from src.errors import ValueResponseError


class ModelObjectInfo2(BaseModel):
    person: ItemsPerson
    qa_salary_after_1_5_year: float = Field(alias="qa_salary_after_1.5_year")
    qa_salary_after_12_months: float
    qa_salary_after_3_5_years: float = Field(alias="qa_salary_after_3.5_years")
    qa_salary_after_6_months: int
    start_qa_salary: int

    @field_validator("qa_salary_after_1_5_year")
    @classmethod
    def check_value_qa_salary_after_1_5_year(cls, value_salary):
        logger.info("Check value qa_salary_after_1_5_year object_info_2")
        if value_salary != (PAYLOAD_TOTAL.get("salary") * 3.3):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("qa_salary_after_12_months")
    @classmethod
    def check_value_qa_salary_after_12_months(cls, value_salary):
        logger.info("Check value qa_salary_after_12_months object_info_2")
        if value_salary != (PAYLOAD_TOTAL.get("salary") * 2.7):
            raise ValueError(ValueResponseError.Error.value)


    @field_validator("qa_salary_after_3_5_years")
    @classmethod
    def check_value_qa_salary_after_3_5_years(cls, value_salary):
        logger.info("Check value qa_salary_after_3_5_years object_info_2")
        if value_salary != (PAYLOAD_TOTAL.get("salary") * 3.8):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("qa_salary_after_6_months")
    @classmethod
    def check_value_qa_salary_after_6_months(cls, value_salary):
        logger.info("Check value qa_salary_after_6_months object_info_2")
        if value_salary != (PAYLOAD_TOTAL.get("salary") * 2):
            raise ValueError(ValueResponseError.Error.value)

    @field_validator("start_qa_salary")
    @classmethod
    def check_value_start_qa_salary(cls, value_salary):
        logger.info("Check value start_qa_salary object_info_2")
        if value_salary != PAYLOAD_TOTAL.get("salary"):
            raise ValueError(ValueResponseError.Error.value)


# Getting json schema
json_schema_object_info_2 = ModelObjectInfo2.model_json_schema()