from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.selectors import DashboardSelectors

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_url = "https://compassioncarehealthclinic.patient7.app/branch/6d9b345f-3f82-41fa-a7c9-881f343c7103/dashboard"

    def load_dashboard(self):
        self.driver.get(self.dashboard_url)

    def get_welcome_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DashboardSelectors.WELCOME_MESSAGE))
        ).text

    def navigate_to_patient_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DashboardSelectors.PATIENT_LIST_BUTTON))
        ).click()
