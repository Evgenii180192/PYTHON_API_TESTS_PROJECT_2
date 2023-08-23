"""The module contains methods for testing sending a request endpoint object_info_4"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_object_info_4.conftest_object_info_4.conftest_object_info_4 import request_object_info_4
from src.models.model_object_info_4.model_info_4 import json_schema_object_info_4, ModelObjectInfo4
from src.headers import headers


def test_check_status_code_object_info_4(request_object_info_4):
    logger.info("Check status code object info 4")
    BaseResponse(request_object_info_4).validate_status_code(status_code=200)


def test_check_json_schema_object_info_4(request_object_info_4):
    logger.info("Check json schema object info 4")
    BaseResponse(request_object_info_4).validate_json_schema(json_schema=json_schema_object_info_4)


def test_check_value_response_object_info_4(request_object_info_4):
    logger.info("Check value response object info 4")
    BaseResponse(request_object_info_4).validate_value_response(model=ModelObjectInfo4)


def test_check_response_headers_object_info_4(request_object_info_4):
    logger.info("Check response headers object info 4")
    BaseResponse(request_object_info_4).validate_response_headers(headers=headers)
