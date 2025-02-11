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
        
        
        # yopmail_email = f"{patient_data['first_name'].lower()}{patient_data['last_name'].lower()}@yopmail.com"
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, AddUserSelectors.EMAIL))
        # ).send_keys(yopmail_email)
  

        print("-------------Email entered------------------", patient_data["email"]) 
        

        
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddUserSelectors.SAVE_BUTTON))
        ).click()
      
      
      
        
        # Open Yopmail
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.yopmail_url)
        
        
        yopmail_email = patient_data["email"]
        print("yopmail_email", yopmail_email)
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, AddUserSelectors.YOPMAIL))
        # ).send_keys(yopmail_email)
        # print("User form submitted. Now checking Yopmail for confirmation email...")

        # Enter the Yopmail email
        email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "login"))
            )
        email_input.send_keys(yopmail_email)
        email_input.submit()

      
        time.sleep(3)

        # first_email = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/div[2]"))
        #     )
        # first_email.click()

        # # Switch to email content frame
        # self.driver.switch_to.default_content()
        # WebDriverWait(self.driver, 10).until(
        # EC.frame_to_be_available_and_switch_to_it((By.ID, "ifmail"))
        #     )

        # Click verification link (modify the XPATH based on actual email content)
        # time.sleep(3)
        # verification_link = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/div[2]/span/a"))
        #     )
        # verification_link.click()
            
        # print("Verification email clicked successfully.")

        # # Switch back to main window
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # print("Returning to user form page.")

        time.sleep(3)
       
        
        
