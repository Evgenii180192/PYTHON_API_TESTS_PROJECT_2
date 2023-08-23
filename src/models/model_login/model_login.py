from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ValueResponseError


class ModelLogin(BaseModel):
    token: str

    @field_validator("token")
    @classmethod
    def check_value_token_login(cls, value_token):
        logger.info("Check value token login")
        with open("D:\python_tests_api_for_homework\src\data_token.py", 'w') as file:
            logger.info("Writing the value of the token parameter to a file dat_token.py")
            file.write(f"token = \"{value_token}\"")
            file.close()
        if not isinstance(value_token, str):
            raise ValueError(ValueResponseError.Error.value)


# Getting json schema
json_schema_login = ModelLogin.model_json_schema()
