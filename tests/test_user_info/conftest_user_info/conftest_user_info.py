import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_USER_INFO
from src.errors import TimeRequestError


@pytest.fixture()
def request_user_info():
    try:
        logger.info("Send request user info")
        response = requests.post(url=BASE_URL + "/user_info",
                                 json=PAYLOAD_USER_INFO,
                                 timeout=5)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response
