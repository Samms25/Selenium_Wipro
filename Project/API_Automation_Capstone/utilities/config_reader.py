import configparser
import os


class ConfigReader:

    def __init__(self):
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_base_url(self):
        return self.config["API"]["base_url"]

    def get_users_endpoint(self):
        return self.config["API"]["users_endpoint"]

    def get_login_endpoint(self):
        return self.config["API"]["login_endpoint"]

    def get_timeout(self):
        return int(self.config["TEST"]["timeout"])