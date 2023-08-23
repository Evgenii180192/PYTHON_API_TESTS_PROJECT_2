"""The module contains methods for testing sending a request endpoint login"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_login.conftest_login.conftest_login import request_login
from src.models.model_login.model_login import json_schema_login, ModelLogin
from src.headers import headers


def test_check_status_code_login(request_login):
    logger.info("Check status code login")
    BaseResponse(request_login).validate_status_code(status_code=200)


def test_check_json_schema_login(request_login):
    logger.info("Check json schema login")
    BaseResponse(request_login).validate_json_schema(json_schema=json_schema_login)


def test_check_value_response_login(request_login):
    logger.info("Check value response login")
    BaseResponse(request_login).validate_value_response(model=ModelLogin)


def test_check_response_headers_login(request_login):
    logger.info("Check response headers login")
    BaseResponse(request_login).validate_response_headers(headers=headers)
