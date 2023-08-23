"""The module contains methods for testing sending a request endpoint test_pet_info"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_pet_info.conftest_test_pet_info.conftest_test_pet_info import request_test_pet_info
from src.models.model_test_pet_info.model_test_pet_info import json_schema_test_pet_info, ModelTestPetInfo
from src.headers import headers


def test_check_status_code_test_pet_info(request_test_pet_info):
    logger.info("Check status code test pet info")
    BaseResponse(request_test_pet_info).validate_status_code(status_code=200)


def test_check_json_schema_test_pet_info(request_test_pet_info):
    logger.info("Check json schema test pet info")
    BaseResponse(request_test_pet_info).validate_json_schema(json_schema=json_schema_test_pet_info)


def test_check_value_response_test_pet_info(request_test_pet_info):
    logger.info("Check value response test pet info")
    BaseResponse(request_test_pet_info).validate_value_response(model=ModelTestPetInfo)


def test_check_response_headers_test_pet_info(request_test_pet_info):
    logger.info("Check response headers test pet info")
    BaseResponse(request_test_pet_info).validate_response_headers(headers=headers)
