import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_TOTAL
from src.errors import TimeRequestError


@pytest.fixture()
def request_user_info_2():
    try:
        logger.info("Send request user info 2")
        response = requests.post(url=BASE_URL + "/user_info_2", data=PAYLOAD_TOTAL, timeout=10)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response




