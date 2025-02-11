# import pytest
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import uuid
# import tempfile
# from webdriver_manager.chrome import ChromeDriverManager
# from session_manager import load_session, perform_login, verify_login

# @pytest.fixture(scope="session")
# def browser():
#     """Set up WebDriver instance with WebDriver Manager"""
#     chrome_options = Options()
    
#     # Create a temporary directory for user data
#     temp_dir = tempfile.mkdtemp()
#     unique_user_data_dir = os.path.join(temp_dir, f"chrome-data-{uuid.uuid4()}")
#     chrome_options.add_argument(f"--user-data-dir={unique_user_data_dir}")

#     # Required options for GitHub Actions
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1920x1080")

#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#         driver.maximize_window()
#         print("✅ ChromeDriver successfully initialized!")
#         yield driver
#     except Exception as e:
#         print(f"❌ ChromeDriver initialization failed: {str(e)}")
#         raise
#     finally:
#         try:
#             driver.quit()
#         except:
#             pass
#         # Cleanup temporary directory
#         try:
#             import shutil
#             shutil.rmtree(temp_dir, ignore_errors=True)
#         except:
#             pass

# @pytest.fixture(scope="session")
# def authenticated_browser(browser):
#     """Handle session-based authentication"""
#     session_files_exist = os.path.exists('cookies.json') and os.path.exists('storage.json')
    
#     if session_files_exist:
#         print("🔄 Found existing session data, attempting to restore...")
#         if load_session(browser) and verify_login(browser):
#             print("✅ Session restored successfully!")
#             return browser
#         else:
#             print("⚠️ Session restoration failed, performing new login...")
    
#     perform_login(browser)
#     return browser

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Capture screenshot on test failure"""
#     outcome = yield
#     report = outcome.get_result()
    
#     if report.failed:
#         driver = item.funcargs.get("browser")
#         if driver:
#             os.makedirs("screenshots", exist_ok=True)
#             screenshot_path = os.path.join("screenshots", f"{item.name}.png")
#             try:
#                 driver.save_screenshot(screenshot_path)
#                 print(f"🖼️ Screenshot saved: {screenshot_path}")
#             except Exception as e:
#                 print(f"⚠️ Screenshot capture failed: {str(e)}")


import pytest
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import uuid
import tempfile
from webdriver_manager.chrome import ChromeDriverManager
from session_manager import load_session, perform_login, verify_login

@pytest.fixture(scope="session")
def browser():
    """Set up WebDriver instance with WebDriver Manager and Allure reporting"""
    with allure.step("Initialize WebDriver"):
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
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.maximize_window()
            allure.attach("ChromeDriver initialized successfully!", name="WebDriver Info", attachment_type=allure.attachment_type.TEXT)
            print("✅ ChromeDriver successfully initialized!")
            yield driver
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="WebDriver Error", attachment_type=allure.attachment_type.TEXT)
            print(f"❌ ChromeDriver initialization failed: {str(e)}")
            raise
        finally:
            with allure.step("Close WebDriver"):
                try:
                    driver.quit()
                    allure.attach("ChromeDriver closed successfully!", name="WebDriver Teardown", attachment_type=allure.attachment_type.TEXT)
                except Exception as e:
                    allure.attach(f"Error closing driver: {str(e)}", name="Teardown Error", attachment_type=allure.attachment_type.TEXT)
                
                # Cleanup temporary directory
                try:
                    import shutil
                    shutil.rmtree(temp_dir, ignore_errors=True)
                except Exception as e:
                    allure.attach(f"Error cleaning temp dir: {str(e)}", name="Cleanup Error", attachment_type=allure.attachment_type.TEXT)

@pytest.fixture(scope="session")
def authenticated_browser(browser):
    """Handle session-based authentication with Allure reporting"""
    with allure.step("Check for existing session"):
        session_files_exist = os.path.exists('cookies.json') and os.path.exists('storage.json')

    if session_files_exist:
        with allure.step("Attempting to restore session"):
            print("🔄 Found existing session data, attempting to restore...")
            if load_session(browser) and verify_login(browser):
                allure.attach("Session restored successfully!", name="Session Info", attachment_type=allure.attachment_type.TEXT)
                print("✅ Session restored successfully!")
                return browser
            else:
                allure.attach("Session restoration failed, performing new login", name="Session Failure", attachment_type=allure.attachment_type.TEXT)
                print("⚠️ Session restoration failed, performing new login...")

    with allure.step("Performing new login"):
        perform_login(browser)
        allure.attach("New session login successful!", name="Login Info", attachment_type=allure.attachment_type.TEXT)
    
    return browser

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure and attach to Allure"""
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")
            try:
                driver.save_screenshot(screenshot_path)
                allure.attach.file(screenshot_path, name=f"Screenshot-{item.name}", attachment_type=allure.attachment_type.PNG)
                print(f"🖼️ Screenshot saved: {screenshot_path}")
            except Exception as e:
                allure.attach(f"Screenshot capture failed: {str(e)}", name="Screenshot Error", attachment_type=allure.attachment_type.TEXT)
                print(f"⚠️ Screenshot capture failed: {str(e)}")
