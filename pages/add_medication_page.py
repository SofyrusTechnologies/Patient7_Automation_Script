import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selectors import AddMedicationSelector
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from faker import Faker
import random

fake = Faker()

class OverViewPage:
    def __init__(self, driver):
        self.driver = driver
 
        self.dashboard_url = "https://lifetreeclinic.patient7.co/branch/f88f5e98-ff35-4499-9dd9-7cae9f4aa137/patient-table/patient-details/b058892a-5a25-457a-924d-b76eef70da02/Overview"
        
    def load_dashboard(self):
        self.driver.get(self.dashboard_url)
   
    def get_mrn_no(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddMedicationSelector.MRN_NO))
        ).text
        
    def enter_medication_details(self):
        medication_name = fake.word()
        dosage = random.randint(1, 500)  # Dosage in mg
        frequency = random.choice(["Once a day", "Twice a day", "Every 6 hours"])
        
        print("medication_name: ", medication_name)
        print("dosage: ", dosage)
        print("frequency: ", frequency)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddMedicationSelector.MEDICATION_NAME))
        ).send_keys(medication_name)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddMedicationSelector.DOSAGE))
        ).send_keys(dosage)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AddMedicationSelector.FREQUENCY))
        ).send_keys(frequency)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, AddMedicationSelector.ADD_MEDICATION))
        ).click()
        
        time.sleep(3)  # Allow time for the medication to be added
        print(f"Added Medication: {medication_name}, Dosage: {dosage}mg, Frequency: {frequency}")
    
    # def verify_medication_added(self):
    #     try:
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, AddMedicationSelector.MEDICATION_ELEMENT))
    #         )
    #         print("Medication added successfully!")
    #     except:
    #         print("Failed to add medication.")

    

    
