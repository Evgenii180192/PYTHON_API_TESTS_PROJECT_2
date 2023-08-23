import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_GET_METHOD
from src.errors import TimeRequestError


@pytest.fixture()
def request_get_method():
    try:
        logger.info("Send request get_method")
        response = requests.get(url=BASE_URL + "/get_method",
                                params=PAYLOAD_GET_METHOD,
                                timeout=2)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response
