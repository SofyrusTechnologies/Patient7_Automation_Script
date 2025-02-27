from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selectors import AddUserSelectors
import time

class AddUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_url = "https://compassioncarehealthclinic.patient7.app/branch/6d9b345f-3f82-41fa-a7c9-881f343c7103/settings/clinic/manage-user"
        self.yopmail_url = "https://yopmail.com"
        
    def load_dashboard(self):
        self.driver.get(self.dashboard_url)
        
    def Get_manage_user_Account(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.GetUserInformation))
        )
        
        time.sleep(5)
    
    def Click_AddUser(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.Click_AddUser))
        ).click()
                
        time.sleep(5)
        
    def fill_user_form(self, patient_data):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.FIRST_NAME))
        ).send_keys(patient_data["first_name"])
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.LAST_NAME))
        ).send_keys(patient_data["last_name"])
                
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.ROLE))
        ).click()
                
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.SELECT_ROLE))
        ).click()
                 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.EMAIL))
        ).send_keys(patient_data["email"])
                         
        print("-------------Email entered------------------", patient_data["email"])
                 
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.SAVE_BUTTON))
        ).click()
        
    def handle_yopmail_workflow(self, patient_data):
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Open Yopmail
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.yopmail_url)
        
          # Block Ads in Yopmail by executing JavaScript
        self.driver.execute_script("""
            var ads = document.querySelectorAll('iframe, .ad, .adsbygoogle, .ad-container');
            ads.forEach(ad => ad.remove());
        """)
        
        # Enter the Yopmail email
        yopmail_email = patient_data["email"]
        print("yopmail_email", yopmail_email)
        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login"))
        )
        email_input.send_keys(yopmail_email)
        email_input.submit()
        time.sleep(3)
        
        # Switch to inbox iframe
        self.driver.switch_to.frame("ifinbox")
        
        # Find and click the email from notifications@patient7.com
        email_from_patient7 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'notifications@patient7.com')]"))
        )
        email_from_patient7.click()
        
        # Switch back to default content and then to mail content iframe
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("ifmail")
        
        # Find and click the Set Password button
        set_password_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Set Password')]"))
        )
        set_password_link = set_password_button.get_attribute("href")
        
        # Open Set Password link in a new tab
        self.driver.execute_script(f"window.open('{set_password_link}', '_blank');")
        
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[2])
        
        # Set the password
        password = "Test@123"  # You might want to parametrize this
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div/div[1]/div/div/div/div[1]/input"))
        ).send_keys(password)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div/div[2]/div/div/div/div[1]/input"))
        ).send_keys(password)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div/button/div/span"))
        ).click()
        
  
        time.sleep(1)
        
        print("User added successfully!")
     
        
