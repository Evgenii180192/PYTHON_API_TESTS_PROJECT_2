"""The module contains methods for testing sending a request endpoint get_test_user"""

from loguru import logger

from src.base_response import BaseResponse
from src.models.model_get_test_user.model_get_test_user import json_schema_get_test_user, ModelGetTestUser
from src.headers import headers
from tests.test_get_test_user.conftest_get_test_user.conftest_get_test_user import request_get_test_user


def test_check_status_code_get_test_user(request_get_test_user):
    logger.info("Check status get test user")
    BaseResponse(request_get_test_user).validate_status_code(status_code=200)


def test_check_json_schema_get_test_user(request_get_test_user):
    logger.info("Check json schema get test user")
    BaseResponse(request_get_test_user).validate_json_schema(json_schema=json_schema_get_test_user)


def test_check_value_response_get_test_user(request_get_test_user):
    logger.info("Check value response get test user")
    BaseResponse(request_get_test_user).validate_value_response(model=ModelGetTestUser)


def test_check_response_headers_get_test_user(request_get_test_user):
    logger.info("Check response headers get test user")
    BaseResponse(request_get_test_user).validate_response_headers(headers=headers)


