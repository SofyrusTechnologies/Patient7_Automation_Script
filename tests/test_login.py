# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# @pytest.fixture(scope="session")
# def logged_in_browser(browser):
#     # Login only once per session
#     browser.get("https://tenderclinic.pt7.io/auth/login")
    
#     # Perform Login
#     email_field = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div[1]/div/input"))
#     )
#     email_field.send_keys("tinki@yopmail.com")

#     password_field = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/input"))
#     )
#     password_field.send_keys("Hello@123")

#     login_button = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/button/div"))
#     )
#     login_button.click()
    
#     select_branch = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/a/div"))
#     )
#     select_branch.click()
    
#     return browser

# def test_login_successful(logged_in_browser):
#     # Basic login test to verify the fixture works
#     assert logged_in_browser.current_url != "https://tenderclinic.pt7.io/auth/login"


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import uuid
import os

@pytest.fixture(scope="session")
def browser():
    """Initialize Chrome WebDriver with proper options for CI environment"""
    chrome_options = Options()
    
    # Create a temporary directory for user data
    temp_dir = tempfile.mkdtemp()
    unique_user_data_dir = os.path.join(temp_dir, f"chrome-data-{uuid.uuid4()}")
    chrome_options.add_argument(f"--user-data-dir={unique_user_data_dir}")
    
    # Required options for GitHub Actions
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        driver.maximize_window()
        print("✅ ChromeDriver successfully initialized!")
        yield driver
    except Exception as e:
        print(f"❌ ChromeDriver initialization failed: {str(e)}")
        raise
    finally:
        try:
            driver.quit()
        except:
            pass
        # Cleanup temporary directory
        try:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)
        except:
            pass

@pytest.fixture(scope="session")
def logged_in_browser(browser):
    """Perform login and handle branch selection"""
    try:
        # Navigate to login page
        browser.get("https://compassioncarehealthclinic.patient7.app/auth/login")
        print("✅ Navigated to login page")
        
        # Login steps with explicit waits and error handling
        email_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, 
                "/html/body/div[1]/div[2]/div[2]/div/div/form/div[1]/div/input"))
        )
        email_field.send_keys("haseen512@yopmail.com")
        print("✅ Email entered")

        password_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, 
                "/html/body/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/input"))
        )
        password_field.send_keys("Hello@123")
        print("✅ Password entered")

        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
                "/html/body/div[1]/div[2]/div[2]/div/div/form/button/div"))
        )
        login_button.click()
        print("✅ Login button clicked")
        
        # Wait for and click branch selection
        select_branch = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
                "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/a/div"))
        )
        select_branch.click()
        print("✅ Branch selected")
        
        return browser
    
    except Exception as e:
        print(f"❌ Login process failed: {str(e)}")
        # Capture screenshot on failure
        try:
            os.makedirs("screenshots", exist_ok=True)
            browser.save_screenshot("screenshots/login_failure.png")
            print("✅ Failure screenshot captured")
        except:
            print("❌ Failed to capture failure screenshot")
        raise

def test_login_successful(logged_in_browser):
    """Verify successful login"""
    try:
        # Wait for URL to change and verify
        WebDriverWait(logged_in_browser, 10).until(
            lambda driver: driver.current_url != "https://compassioncarehealthclinic.patient7.app/auth/login"
        )
        
        assert logged_in_browser.current_url != "https://compassioncarehealthclinic.patient7.app/auth/login"
        print("✅ Login test passed")
        
    except Exception as e:
        print(f"❌ Login verification failed: {str(e)}")
        raise