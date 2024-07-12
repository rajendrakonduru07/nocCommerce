import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Login_page_admin
from base_pages.Add_Customer_Page import Add_Customer_Page
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_maker



class Test_02_Add_new_Customer:

    page_url = Read_config.get_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    logger =Log_maker.log_gen()


    @pytest.mark.regression
    def test_addNew_Customer(self,setup):
        self.logger.info("===========Test_02_Add_new_Customer started=========")
        self.logger.info("======Login to Application started ======")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.page_url)
        self.driver.maximize_window()
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
        self.logger.info("=================Login Completed====================")
        self.logger.info("=================adding new customer started====================")
        self.add_cutomer = Add_Customer_Page(self.driver)
        self.add_cutomer.click_customer()
        self.add_cutomer.click_submenu_customer()
        self.add_cutomer.click_add_new()
        self.add_cutomer.entering_email("rajendra.konduru@gmail.com")
        self.add_cutomer.entering_password("rajendra@123")
        self.add_cutomer.entering_firstname("Rajendra")
        self.add_cutomer.entering_lastname("konduru")
        self.add_cutomer.select_genger("Male")
        self.add_cutomer.select_dataofbirth("07/10/1991")
        self.add_cutomer.entering_company_name("HCL Tech")
        self.add_cutomer.select_tax_exempt()
        self.add_cutomer.select_active()
        self.add_cutomer.entering_Admin_comment(" Hello Admin Comment test")
        self.add_cutomer.click_save()
        success_msg = "The new customer has been added successfully."
        if success_msg == self.driver.find_element(By.XPATH,"class ='content-wrapper']/div[1]").text :
            assert True
            self.logger.info("Adding new customer complted")
        else :
            assert False
            self.logger.info("Adding new customer Failed")

        self.logger.info("===========Test_02_Add_new_Customer Completed=========")
        self.logger.info("=================adding new customer completed====================")












