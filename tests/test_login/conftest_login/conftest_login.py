import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_LOGIN
from src.errors import TimeRequestError


@pytest.fixture()
def request_login():
    try:
        logger.info("Send request login")
        response = requests.post(url=BASE_URL + "/login",
                                 data=PAYLOAD_LOGIN,
                                 timeout=5)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response