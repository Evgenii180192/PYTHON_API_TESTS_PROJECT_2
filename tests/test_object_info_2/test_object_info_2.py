"""The module contains methods for testing sending a request endpoint object_info_2"""

from loguru import logger
from tests.test_object_info_2.conftest_object_info_2.conftest_object_info_2 import request_object_info_2
from src.base_response import BaseResponse
from src.models.model_object_info_2.model_object_info_2 import json_schema_object_info_2, ModelObjectInfo2
from src.headers import headers


def test_check_status_code_object_info_2(request_object_info_2):
    logger.info("Check status code object info 2")
    BaseResponse(request_object_info_2).validate_status_code(status_code=200)


def test_check_json_schema_object_info_2(request_object_info_2):
    logger.info("Check json schema object info 2")
    BaseResponse(request_object_info_2).validate_json_schema(json_schema=json_schema_object_info_2)


def test_check_value_response_object_info_2(request_object_info_2):
    logger.info("Check value response object info 2")
    BaseResponse(request_object_info_2).validate_value_response(model=ModelObjectInfo2)


def test_check_response_headers_object_info_2(request_object_info_2):
    logger.info("Check response headers object info 2")
    BaseResponse(request_object_info_2).validate_response_headers(headers=headers)
