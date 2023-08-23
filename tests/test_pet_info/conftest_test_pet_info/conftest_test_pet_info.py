import pytest
import requests
from loguru import logger
from requests import Timeout

from src.configuration import BASE_URL, PAYLOAD_TEST_PET_INFO
from src.errors import TimeRequestError


@pytest.fixture()
def request_test_pet_info():
    try:
        logger.info("Send request test pet info")
        response = requests.post(url=BASE_URL + "/test_pet_info",
                                 data=PAYLOAD_TEST_PET_INFO,
                                 timeout=2)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    return response
