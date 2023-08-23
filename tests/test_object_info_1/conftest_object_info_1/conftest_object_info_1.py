import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_OBJECT_INFO_1
from src.errors import TimeRequestError


@pytest.fixture()
def request_object_info_1():
    try:
        logger.info("Send request object info 1")
        response = requests.get(url=BASE_URL + "/object_info_1",
                                params=PAYLOAD_OBJECT_INFO_1,
                                timeout=2)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response
