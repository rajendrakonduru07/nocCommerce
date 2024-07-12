import configparser


config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:
    @staticmethod
    def get_page_url():
        url = config.get('login info','page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('login info', 'password')
        return password

