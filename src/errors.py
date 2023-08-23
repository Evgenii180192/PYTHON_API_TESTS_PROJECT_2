from enum import Enum


class StatusCodeError(Enum):
    Error = "The current status of the code does not match what is expected"


class JSONSchemaError(Enum):
    Error = "JSON schema of response from server does not match expected"


class ValueResponseError(Enum):
    Error = "Values in the response from the server do not match what is expected"


class HeadersError(Enum):
    Error = "Response headers do not match expected headers"


class TimeRequestError(Enum):
    Error = "Request timed out"


class ResponseTextError(Enum):
    Error = "Response text not as expected"


class SSLError(Enum):
    Error = "Failed to verify certificate"

