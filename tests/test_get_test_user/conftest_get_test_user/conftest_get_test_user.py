import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_TOTAL
from src.errors import TimeRequestError


@pytest.fixture()
def request_get_test_user():
    try:
        logger.info("Send request get test user")
        response = requests.post(url=BASE_URL + "/get_test_user",
                                 data=PAYLOAD_TOTAL,
                                 timeout=2)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response
