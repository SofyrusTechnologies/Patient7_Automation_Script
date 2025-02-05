from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selectors import PatientListSelectors

class PatientListPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_patient_list_loaded(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PatientListSelectors.PAGE_TITLE))
        ).text

    def click_add_patient(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PatientListSelectors.ADD_PATIENT_BUTTON))
        ).click()
