"""The module contains methods for testing sending a request endpoint object_info_3"""

from loguru import logger

from src.base_response import BaseResponse
from tests.test_object_info_3.conftest_object_info_3.conftest_object_Info_3 import request_object_info_3
from src.models.model_object_info_3.model_object_info_3 import json_schema_object_info_3, ModelObjectInfo3
from src.headers import headers


def test_check_status_code_object_info_3(request_object_info_3):
    logger.info("Check status code object info 3")
    BaseResponse(request_object_info_3).validate_status_code(status_code=200)


def test_check_json_schema_object_info_3(request_object_info_3):
    logger.info("Check json schema object info 3")
    BaseResponse(request_object_info_3).validate_json_schema(json_schema=json_schema_object_info_3)


def test_check_value_response_object_info_3(request_object_info_3):
    logger.info("Check value response object info 3")
    BaseResponse(request_object_info_3).validate_value_response(model=ModelObjectInfo3)


def test_check_response_headers_object_info_3(request_object_info_3):
    logger.info("Check response headers object info 3")
    BaseResponse(request_object_info_3).validate_response_headers(headers=headers)
