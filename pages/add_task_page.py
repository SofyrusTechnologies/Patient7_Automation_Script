from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selectors import AddTaskSelectors
import time

class AddTaskPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_url = "https://compassioncarehealthclinic.patient7.app/branch/6d9b345f-3f82-41fa-a7c9-881f343c7103/task?active-tab=active+task"
     
        
    def load_dashboard(self):
        self.driver.get(self.dashboard_url)
        
    def Add_task_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, AddTaskSelectors.ADDTASKBUTTON))
        ).click()
    
        time.sleep(2)
      
    def fill_user_form(self, patient_data):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddTaskSelectors.TASKTITLE))
        ).send_keys(patient_data["first_name"])
        
                 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddTaskSelectors.AASIGNROLE))
        ).click()
                
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddTaskSelectors.SELECTROLE))
        ).click()
                 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddTaskSelectors.TASKTYPE))
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddTaskSelectors.ASSIGNTASK))
        ).click()
        
        time.sleep(3) 
        
        actual_value =  WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddTaskSelectors.ASSERT))
        ).text
        print("Actual Value patient list", actual_value)
        expected_value = patient_data["first_name"] 
        print("Expected Value patient list", expected_value)
        assert actual_value == expected_value, f"Assertion failed: Expected '{expected_value}', but got '{actual_value}'"
        print("Assertion Passed: Patient details opened successfully") 
        
        time.sleep(1) 
            
        
     
    