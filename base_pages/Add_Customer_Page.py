from selenium.webdriver.common.by import By


class Add_Customer_Page:

    link_customer_menu_xpath ="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_submenu_xpah= "(//li[@class='nav-item']//p)[16]"
    add_new_button_xpath ="//div[@class='float-right']/a"
    text_box_email_id = "Email"
    text_box_password_id = "Password"
    text_box_firstname_id = "FirstName"
    text_box_lastname_id = "LastName"
    radio_btn_gender_Male_xpath = "//input[@id='Gender_Male']"
    radio_btn_gender_Female_xpath = "//input[@id='Gender_Female']"
    dat_of_birth_id = "DateOfBirth"
    text_box_companyName_id = "Company"
    check_box_Istaxexempt_id = "IsTaxExempt"
    dropdown_Newsletter_xpath  = "(//span[@role='combobox'])[1]"
    dropdown_Customer_roles_xpath   = "(// span[@ role='combobox'])[2]"
    dropdown_Manager_of_vendor_id = "VendorId"
    check_box_active_id = "Active"
    input_box_admincomment_id = "AdminComment"
    button_save_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver


    def click_customer(self):
        self.driver.find_element(By.XPATH,self.link_customer_menu_xpath).click()

    def click_submenu_customer(self):
        self.driver.find_element(By.XPATH,self.link_customer_submenu_xpah).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH,self.add_new_button_xpath).click()

    def entering_email(self,email):
         self.driver.find_element(By.ID,self.text_box_email_id).click()
         self.driver.find_element(By.ID,self.text_box_email_id).send_keys(email)

    def entering_password(self,password):
        self.driver.find_element(By.ID,self.text_box_password_id).click()
        self.driver.find_element(By.ID,self.text_box_password_id).send_keys(password)

    def entering_firstname(self,firstname):
        self.driver.find_element(By.ID,self.text_box_firstname_id).click()
        self.driver.find_element(By.ID,self.text_box_firstname_id).send_keys(firstname)

    def entering_lastname(self,lastname):
        self.driver.find_element(By.ID,self.text_box_lastname_id).click()
        self.driver.find_element(By.ID,self.text_box_lastname_id).send_keys(lastname)

    def select_genger(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,self.radio_btn_gender_Male_xpath)
        elif gender == "Female":
            self.driver.find_element(By.XPATH,self.radio_btn_gender_Female_xpath)
        else :
            self.driver.find_element(By.XPATH,self.radio_btn_gender_Female_xpath)

    def select_dataofbirth(self,dob):
        self.driver.find_element(By.ID,self.dat_of_birth_id).send_keys(dob)

    def entering_company_name(self,companyname):
        self.driver.find_element(By.ID,self.text_box_companyName_id).click()
        self.driver.find_element(By.ID,self.text_box_companyName_id).send_keys(companyname)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID,self.check_box_Istaxexempt_id).click()

    def select_active(self):
        self.driver.find_element(By.ID,self.check_box_active_id).click()

    def entering_Admin_comment(self,admincomment):
        self.driver.find_element(By.ID,self.input_box_admincomment_id).click()
        self.driver.find_element(By.ID,self.input_box_admincomment_id).send_keys(admincomment)

    def click_save(self):
        try:
            self.driver.find_element(By.XPATH,self.button_save_xpath).click()
        except:
            save_btn = self.driver.find_element(By.XPATH("//button[@name='save']"))
            self.driver.execute_script("arguments[0].click();", save_btn)
















