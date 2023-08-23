"""The module contains methods for testing sending a request endpoint user_info"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_user_info.conftest_user_info.conftest_user_info import request_user_info
from src.models.model_user_info.model_user_info import json_schema_user_info, ModelUserInfo
from src.headers import headers


def test_check_status_code_user_info(request_user_info):
    logger.info("Check status code user info")
    BaseResponse(request_user_info).validate_status_code(status_code=200)


def test_check_json_schema_user_info(request_user_info):
    logger.info("Check json schema user info")
    BaseResponse(request_user_info).validate_json_schema(json_schema=json_schema_user_info)


def test_check_value_response_user_info(request_user_info):
    logger.info("Check value response user info")
    BaseResponse(request_user_info).validate_value_response(model=ModelUserInfo)


def test_check_response_headers_user_info(request_user_info):
    logger.info("Check response headers user info")
    BaseResponse(request_user_info).validate_response_headers(headers=headers)
