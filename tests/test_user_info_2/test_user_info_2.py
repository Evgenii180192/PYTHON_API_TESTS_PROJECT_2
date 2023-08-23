"""The module contains methods for testing sending a request endpoint user_info_2"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_user_info_2.conftest_user_info_2.conftest_user_info_2 import request_user_info_2

from src.models.model_user_info_2.model_user_info_2 import json_schema_user_info_2, ModelUserInfo2
from src.headers import headers


def test_check_status_code_user_info_2(request_user_info_2):
    logger.info("Check status code user info 2")
    BaseResponse(request_user_info_2).validate_status_code(status_code=200)


def test_check_json_schema_user_info_2(request_user_info_2):
    logger.info("Check json schema user info 2")
    BaseResponse(request_user_info_2).validate_json_schema(json_schema=json_schema_user_info_2)


def test_check_value_response_user_info_2(request_user_info_2):
    logger.info("Check value response user info 2")
    BaseResponse(request_user_info_2).validate_value_response(model=ModelUserInfo2)


def test_check_response_headers_user_info_2(request_user_info_2):
    logger.info("Check response headers user info 2")
    BaseResponse(request_user_info_2).validate_response_headers(headers=headers)
