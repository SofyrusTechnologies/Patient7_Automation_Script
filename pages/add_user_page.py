# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utils.selectors import AddUserSelectors
# import time

# class AddUserPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.dashboard_url = "https://lifetreeclinic.patient7.co/branch/f88f5e98-ff35-4499-9dd9-7cae9f4aa137/settings/clinic/manage-user"
#         self.yopmail_url = "https://yopmail.com"
        
#     def load_dashboard(self):
#         self.driver.get(self.dashboard_url)
        
#     def Get_manage_user_Account(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.GetUserInformation))
#         )
        
#     time.sleep(2)
    
#     def Click_AddUser(self):
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.Click_AddUser))
#         ).click()
        
#         time.sleep(2)
    

#     def fill_user_form(self, patient_data):
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.FIRST_NAME))
#         ).send_keys(patient_data["first_name"])

#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.LAST_NAME))
#         ).send_keys(patient_data["last_name"])
        
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.ROLE))
#         ).click()
        
#         time.sleep(2)
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.SELECT_ROLE))
#         ).click()
        

#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.EMAIL))
#         ).send_keys(patient_data["email"])
        
        
#         print("-------------Email entered------------------", patient_data["email"]) 
        
#         time.sleep(2)
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, AddUserSelectors.SAVE_BUTTON))
#         ).click()
      
      
      
        
#         # Open Yopmail
#         self.driver.execute_script("window.open('');")
#         self.driver.switch_to.window(self.driver.window_handles[1])
#         self.driver.get(self.yopmail_url)
        
        
#         yopmail_email = patient_data["email"]
#         print("yopmail_email", yopmail_email)
     
#         # Enter the Yopmail email
#         email_input = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "login"))
#             )
#         email_input.send_keys(yopmail_email)
#         email_input.submit()
#         time.sleep(3)
       
       
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selectors import AddUserSelectors
import time

class AddUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_url = "https://lifetreeclinic.patient7.co/branch/f88f5e98-ff35-4499-9dd9-7cae9f4aa137/settings/clinic/manage-user"
        self.yopmail_url = "https://yopmail.com"
        
    def load_dashboard(self):
        self.driver.get(self.dashboard_url)
        
    def Get_manage_user_Account(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.GetUserInformation))
        )
        
        time.sleep(2)
    
    def Click_AddUser(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.Click_AddUser))
        ).click()
                
        time.sleep(2)
        
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
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys(password)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "confirmPassword"))
        ).send_keys(password)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Set Password')]"))
        ).click()
        
        # Switch back to original tab
        self.driver.switch_to.window(original_window)
        
    def verify_user_added(self, patient_data):
        # Wait for the user list to refresh
        time.sleep(3)
        
        # Look for the newly added user in the list
        user_xpath = f"//td[contains(text(), '{patient_data['email']}')]"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, user_xpath))
            )
            print(f"User {patient_data['email']} was successfully added!")
            return True
        except:
            print(f"Failed to find user {patient_data['email']} in the list!")
            return False
        
        
