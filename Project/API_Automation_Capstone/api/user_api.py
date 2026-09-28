import requests

from utilities.config_reader import ConfigReader
from utilities.logger import logger


class UserAPI:

    def __init__(self):
        self.config = ConfigReader()
        self.base_url = self.config.get_base_url()
        self.users_endpoint = self.config.get_users_endpoint()
        self.timeout = self.config.get_timeout()

    def get_all_users(self):
        url = self.base_url + self.users_endpoint

        logger.info(f"GET {url}")

        response = requests.get(
            url,
            timeout=self.timeout
        )

        logger.info(
            f"GET {url} -> Status: {response.status_code}"
        )

        return response

    def get_user_by_id(self, user_id):
        url = f"{self.base_url}{self.users_endpoint}/{user_id}"

        logger.info(f"GET {url}")

        response = requests.get(
            url,
            timeout=self.timeout
        )

        logger.info(
            f"GET {url} -> Status: {response.status_code}"
        )

        return response

    def create_user(self, user_data):
        url = f"{self.base_url}{self.users_endpoint}/add"

        logger.info(f"POST {url}")

        response = requests.post(
            url,
            json=user_data,
            timeout=self.timeout
        )

        logger.info(
            f"POST {url} -> Status: {response.status_code}"
        )

        return response

    def update_user(self, user_id, user_data):
        url = f"{self.base_url}{self.users_endpoint}/{user_id}"

        logger.info(f"PUT {url}")

        response = requests.put(
            url,
            json=user_data,
            timeout=self.timeout
        )

        logger.info(
            f"PUT {url} -> Status: {response.status_code}"
        )

        return response

    def delete_user(self, user_id):
        url = f"{self.base_url}{self.users_endpoint}/{user_id}"

        logger.info(f"DELETE {url}")

        response = requests.delete(
            url,
            timeout=self.timeout
        )

        logger.info(
            f"DELETE {url} -> Status: {response.status_code}"
        )

        return response