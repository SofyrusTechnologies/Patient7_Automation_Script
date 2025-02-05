
# import pytest
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import uuid
# from webdriver_manager.chrome import ChromeDriverManager
# from session_manager import load_session, perform_login, verify_login

# @pytest.fixture(scope="session")
# def browser():
#     """Set up WebDriver instance with WebDriver Manager"""
  
#     chrome_options = Options()

#     # ✅ Generate a unique directory for Chrome to prevent conflicts
#     unique_user_data_dir = f"/tmp/chrome-user-data-{uuid.uuid4()}"
#     chrome_options.add_argument(f"--user-data-dir={unique_user_data_dir}")

#     # ✅ Required options for GitHub Actions
#     chrome_options.add_argument("--headless")  
#     chrome_options.add_argument("--no-sandbox")  
#     chrome_options.add_argument("--disable-dev-shm-usage")  
#     chrome_options.add_argument("--disable-gpu")  
#     chrome_options.add_argument("--window-size=1920x1080")  

#     try:
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#         driver.maximize_window()
#         print("✅ ChromeDriver successfully initialized!")
#     except Exception as e:
#         print(f"❌ ChromeDriver Initialization Failed: {e}")
#         raise

#     yield driver
#     driver.quit()


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
#     """Capture screenshot and record video on test failure"""
#     outcome = yield
#     report = outcome.get_result()

#     if report.failed:
#         driver = item.funcargs.get("browser")  # Get the WebDriver instance
#         if driver:
#             os.makedirs("screenshots", exist_ok=True)
#             screenshot_path = os.path.join("screenshots", f"{item.name}.png")
#             driver.save_screenshot(screenshot_path)
#             print(f"🖼️ Screenshot saved: {screenshot_path}")

#             # ✅ Safe video capture method
#             os.makedirs("videos", exist_ok=True)
#             video_path = os.path.join("videos", f"{item.name}.mp4")
#             try:
#                 os.system(f"ffmpeg -f x11grab -video_size 1920x1080 -i :0.0 -t 10 {video_path} -y")
#                 print(f"🎥 Video recorded: {video_path}")
#             except Exception as e:
#                 print(f"⚠️ Video recording failed: {e}")


import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import uuid
import tempfile
from webdriver_manager.chrome import ChromeDriverManager
from session_manager import load_session, perform_login, verify_login

@pytest.fixture(scope="session")
def browser():
    """Set up WebDriver instance with WebDriver Manager"""
    chrome_options = Options()
    
    # Create a temporary directory for user data
    temp_dir = tempfile.mkdtemp()
    unique_user_data_dir = os.path.join(temp_dir, f"chrome-data-{uuid.uuid4()}")
    chrome_options.add_argument(f"--user-data-dir={unique_user_data_dir}")

    # Required options for GitHub Actions
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
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
def authenticated_browser(browser):
    """Handle session-based authentication"""
    session_files_exist = os.path.exists('cookies.json') and os.path.exists('storage.json')
    
    if session_files_exist:
        print("🔄 Found existing session data, attempting to restore...")
        if load_session(browser) and verify_login(browser):
            print("✅ Session restored successfully!")
            return browser
        else:
            print("⚠️ Session restoration failed, performing new login...")
    
    perform_login(browser)
    return browser

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")
            try:
                driver.save_screenshot(screenshot_path)
                print(f"🖼️ Screenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"⚠️ Screenshot capture failed: {str(e)}")
