from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators (Defined separately for better readability)
    WELCOME_MESSAGE = (By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/div[1]/div")
    TODAY_TOP_CONSULTS = (By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]")
    TODAY_SCHEDULE = (By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div[1]/div[1]")
    MONTHLY_FINANCES = (By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div[2]/div[1]")
    TASKS = (By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[2]/div[2]/div[1]")

    def open_dashboard(self):
        """Navigate to the dashboard page."""
        self.driver.get("https://tenderclinic.pt7.io/branch/cf048f64-0c80-4071-aaa2-8fa960ee6d9b/dashboard")

    def get_text(self, locator):
        """Get text from a given element."""
        return self.wait.until(EC.presence_of_element_located(locator)).text
