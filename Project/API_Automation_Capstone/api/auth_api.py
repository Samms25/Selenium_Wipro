import requests
from utilities.config_reader import ConfigReader


class AuthAPI:

    def __init__(self):
        self.config = ConfigReader()
        self.base_url = self.config.get_base_url()
        self.login_endpoint = self.config.get_login_endpoint()

    def login(self, username, password):

        url = self.base_url + self.login_endpoint

        payload = {
            "username": username,
            "password": password
        }

        response = requests.post(
            url,
            json=payload
        )

        return response