import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_TOTAL
from src.errors import TimeRequestError


@pytest.fixture()
def request_new_data():
    try:
        logger.info("Send request new dat")
        response = requests.post(url=BASE_URL + "/new_data",
                                 data=PAYLOAD_TOTAL,
                                 timeout=2)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response
