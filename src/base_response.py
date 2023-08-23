"""The class contains methods for processing the response from the server"""

from jsonschema import validate
from loguru import logger
from requests import JSONDecodeError

from src.errors import StatusCodeError, JSONSchemaError, ValueResponseError, HeadersError, ResponseTextError


class BaseResponse:

    def __init__(self, response):
        """Initializing the response from the server"""
        self.response = response
        try:
            self.response_json = response.json()
        except JSONDecodeError:
            logger.info("Response not in JSON format")
        self.response_status_code = response.status_code
        self.response_headers = response.headers
        self.response_text = response.text
        request_time = self.response_elapsed = response.elapsed
        logger.info(f"Request time: {request_time}")

    def validate_status_code(self, status_code):
        """The method for checking response code status"""
        assert self.response_status_code == status_code, StatusCodeError.Error.value
        return self

    def validate_json_schema(self, json_schema):
        """The method check json - schema from response"""
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, json_schema), JSONSchemaError.Error.value
        else:
            validate(self.response_json, json_schema), JSONSchemaError.Error.value
        return self

    def validate_value_response(self, model):
        """The method to validate values from response"""
        if isinstance(self.response_json, list):
            for item in self.response_json:
                model.model_validate(item), ValueResponseError.Error.value
        else:
            model.model_validate(self.response_json), ValueResponseError.Error.value
        return self

    def validate_response_headers(self, headers):
        """The method for checking headers from response"""
        for item_headers in self.response_headers:
            if item_headers not in headers:
                raise ValueError(HeadersError.Error.value)
        return self

    def validate_response_text(self, text):
        """The method check text from response"""
        assert self.response_text == text, ResponseTextError.Error.value
        return self


