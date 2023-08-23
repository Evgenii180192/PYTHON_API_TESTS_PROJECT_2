"""The module contains methods for testing sending a request endpoint new_data"""

from loguru import logger

from src.headers import headers
from tests.test_new_data.conftest_new_data.conftest_new_data import request_new_data
from src.models.model_new_data.model_new_data import json_schema_new_data, ModelNewData
from src.base_response import BaseResponse


def test_check_status_code_new_data(request_new_data):
    logger.info("Check status code new data")
    BaseResponse(request_new_data).validate_status_code(status_code=200)


def test_check_json_schema_new_data(request_new_data):
    logger.info("Check json schema new data")
    BaseResponse(request_new_data).validate_json_schema(json_schema=json_schema_new_data)


def test_check_value_response_new_data(request_new_data):
    logger.info("Check value response new data")
    BaseResponse(request_new_data).validate_value_response(model=ModelNewData)


def test_check_response_headers_new_data(request_new_data):
    logger.info("Check response headers new data")
    BaseResponse(request_new_data).validate_response_headers(headers=headers)