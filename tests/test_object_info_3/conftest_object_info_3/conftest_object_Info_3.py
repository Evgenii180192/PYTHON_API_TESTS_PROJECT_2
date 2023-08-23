import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_TOTAL
from src.errors import TimeRequestError


@pytest.fixture()
def request_object_info_3():
    try:
        logger.info("Send request object info 3")
        response = requests.get(url=BASE_URL + "/object_info_3",
                                params=PAYLOAD_TOTAL,
                                timeout=2)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response
