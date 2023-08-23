import pytest
import requests
from loguru import logger
from requests import Timeout
from requests.exceptions import SSLError

from src.configuration import BASE_URL
from src.errors import TimeRequestError


@pytest.fixture()
def request_first():
    try:
        logger.info("Send request first")
        response = requests.get(url=BASE_URL + "/first",
                                verify=True,
                                timeout=2)
    except Timeout:
        raise ValueError(TimeRequestError.Error.value)
    except SSLError:
        raise ValueError(SSLError.Error.value)
    return response