"""The module contains methods for testing sending a request endpoint get_method"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_get_method.conftest_get_method.conftest_get_method import request_get_method
from src.headers import headers


def test_check_status_code_get_method(request_get_method):
    logger.info("Check status code get_method")
    BaseResponse(request_get_method).validate_status_code(status_code=200)


def test_check_response_headers_get_method(request_get_method):
    logger.info("Check response headers get_method")
    BaseResponse(request_get_method).validate_response_headers(headers=headers)
