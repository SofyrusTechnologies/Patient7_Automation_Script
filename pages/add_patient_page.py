from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selectors import AddPatientSelectors
import time

class AddPatientPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_patient_form(self, patient_data):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.FIRST_NAME))
        ).send_keys(patient_data["first_name"])

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.LAST_NAME))
        ).send_keys(patient_data["last_name"])

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.DOB))
        ).send_keys(patient_data["dob"])
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.MOBILE))
        ).send_keys(patient_data["mobile_no"])

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.EMAIL))
        ).send_keys(patient_data["email"])

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.ADDRESS))
        ).send_keys(patient_data["address"])
        
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.PATIENT_ELEMENT))
        ).click()
      
        time.sleep(2)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.PATIENT_COLORCODE))
        )
        
        # Assertion: Check Patient List is Loaded
        PATIENT_COLORCODE = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.PATIENT_COLORCODE))
        )
        actual_value = PATIENT_COLORCODE.text
        expected_value = "Color Tag"
        assert actual_value == expected_value, f"Assertion failed: Expected '{expected_value}', but got '{actual_value}'"
        print("Assertion Passed: Color Tag after submitting patient form")  


        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.NEW_PATIENT))
        ).click()

        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.PATIENT_DETAILS))
        ).click()
        
        time.sleep(10)
        
        

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.OPEN_PATIENT_DETAILS))
        )
        
        # Assertion: Check Patient List is Loaded
        PATIENT_COLORCODE = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddPatientSelectors.OPEN_PATIENT_DETAILS))
        )
        actual_value = PATIENT_COLORCODE.text
        print("Actual Value patient list" , actual_value)
        expected_value = patient_data["first_name"] + " " + patient_data["last_name"]
        print("Expected Value patient list" , expected_value)
        assert actual_value == expected_value, f"Assertion failed: Expected '{expected_value}', but got '{actual_value}'"
        print("Assertion Passed: Patient details opened successfully")  
        
        time.sleep(2)
