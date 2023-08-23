"""The module contains methods for testing sending a request endpoint first"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_first.conftest_first.conftest_first import request_first
from src.headers import headers


def test_check_status_code_first(request_first):
    logger.info("Check status code first")
    BaseResponse(request_first).validate_status_code(status_code=200)


def test_check_response_text_first(request_first):
    logger.info("Check response text first")
    BaseResponse(request_first).validate_response_text(text="This is the first responce from server!ss")


def test_check_response_headers_first(request_first):
    logger.info("Check response headers first")
    BaseResponse(request_first).validate_response_headers(headers=headers)
