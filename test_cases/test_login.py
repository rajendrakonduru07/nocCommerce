import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Login_page_admin
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_maker


class Test_01_Login:

    page_url = Read_config.get_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    logger =Log_maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("===========Test_01_Login started===========")
        self.logger.info("===========verification of page title started===========")
        self.driver= setup
        self.driver.get(self.page_url)
        act_title = self.driver.title
        exp_title ="Your store. Login"
        if exp_title == act_title:
            self.logger.info("======Page title matched======")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("======Page title not matched======")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_login(self,setup):
        self.logger.info("======Validation of login started ======")
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_page = Login_page_admin(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()
        act_dashboard_text =self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_dashboard_text == "Dashboard":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.driver.close()
            assert False

        self.logger.info("===========Test_01_Login Completed===========")
        self.logger.info("======User has been login successfully======")






