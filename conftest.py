import pytest
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import uuid
import tempfile
from webdriver_manager.chrome import ChromeDriverManager
from session_manager import load_session, perform_login, verify_login
import functools
import inspect


@pytest.fixture(scope="session")
def browser():
    """Set up WebDriver instance with WebDriver Manager and Allure reporting."""
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
            allure.attach("ChromeDriver initialized successfully!", 
                         name="WebDriver Info", 
                         attachment_type=allure.attachment_type.TEXT)
            print("✅ ChromeDriver successfully initialized!")
            yield driver
        except Exception as e:
            allure.attach(f"Error: {str(e)}", 
                         name="WebDriver Error", 
                         attachment_type=allure.attachment_type.TEXT)
            print(f"❌ ChromeDriver initialization failed: {str(e)}")
            raise
        finally:
            with allure.step("Close WebDriver"):
                try:
                    driver.quit()
                    allure.attach("ChromeDriver closed successfully!", 
                                name="WebDriver Teardown", 
                                attachment_type=allure.attachment_type.TEXT)
                except Exception as e:
                    allure.attach(f"Error closing driver: {str(e)}", 
                                name="Teardown Error", 
                                attachment_type=allure.attachment_type.TEXT)

                # Cleanup temporary directory
                try:
                    import shutil
                    shutil.rmtree(temp_dir, ignore_errors=True)
                except Exception as e:
                    allure.attach(f"Error cleaning temp dir: {str(e)}", 
                                name="Cleanup Error", 
                                attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope="session" )
def authenticated_browser(browser):
    """Handle session-based authentication with Allure reporting."""
    with allure.step("Check for existing session"):
        session_files_exist = os.path.exists('cookies.json') and os.path.exists('storage.json')

    if session_files_exist:
        with allure.step("Attempting to restore session"):
            print("🔄 Found existing session data, attempting to restore...")
            if load_session(browser) and verify_login(browser):
                allure.attach("Session restored successfully!", 
                            name="Session Info", 
                            attachment_type=allure.attachment_type.TEXT)
                print("✅ Session restored successfully!")
                return browser
            else:
                allure.attach("Session restoration failed, performing new login", 
                            name="Session Failure", 
                            attachment_type=allure.attachment_type.TEXT)
                print("⚠️ Session restoration failed, performing new login...")

    with allure.step("Performing new login"):
        perform_login(browser)
        allure.attach("New session login successful!", 
                     name="Login Info", 
                     attachment_type=allure.attachment_type.TEXT)

    return browser

# Store the current test step
class TestContext:
    current_step = None

def step(description):
    """
    Decorator to track test steps and highlight failures.
    Usage:
    @step("Logging into application")
    def test_login():
        ...
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            TestContext.current_step = description
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Add step information to the exception
                e.step_info = description
                raise
        return wrapper
    return decorator



def highlight_element(driver, element, duration=3):
    """
    Highlight an element on the page with visual effects.
    
    Args:
        driver: WebDriver instance
        element: WebElement to highlight
        duration: How long to show the highlight (seconds)
    """
    original_style = element.get_attribute('style')
    
    # Apply highlight with a more focused visual effect
    driver.execute_script("""
        arguments[0].style.border = '3px solid red';
        arguments[0].style.backgroundColor = 'rgba(255, 0, 0, 0.1)';
        arguments[0].style.boxShadow = '0 0 10px rgba(255, 0, 0, 0.5)';
        arguments[0].style.transition = 'all 0.3s';
        arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});
    """, element)
    
    return original_style

def add_failure_overlay(driver, test_name, failed_step=None, failed_element=None):
    """Add a visible overlay indicating test failure with step information."""
    driver.execute_script("""
        // Create the overlay
        var overlay = document.createElement('div');
        overlay.id = 'test-failure-overlay';
        overlay.style.position = 'fixed';
        overlay.style.top = '10px';
        overlay.style.right = '10px';
        overlay.style.padding = '15px 20px';
        overlay.style.background = 'rgba(255, 0, 0, 0.9)';
        overlay.style.color = 'white';
        overlay.style.borderRadius = '5px';
        overlay.style.zIndex = '10000';
        overlay.style.fontFamily = 'Arial, sans-serif';
        overlay.style.fontSize = '14px';
        overlay.style.boxShadow = '0 2px 4px rgba(0,0,0,0.2)';
        overlay.style.maxWidth = '400px';
        overlay.style.wordWrap = 'break-word';
        
        var content = '<strong>❌ Test Failed:</strong><br/>' + arguments[0];
        if (arguments[1]) {
            content += '<br/><br/><strong>Failed Step:</strong><br/>' + arguments[1];
        }
        
        overlay.innerHTML = content;
        document.body.appendChild(overlay);
        
        // If we have a failed element, create a spotlight effect
        if (arguments[2]) {
            var rect = arguments[2].getBoundingClientRect();
            var spotlight = document.createElement('div');
            spotlight.style.position = 'fixed';
            spotlight.style.top = '0';
            spotlight.style.left = '0';
            spotlight.style.width = '100%';
            spotlight.style.height = '100%';
            spotlight.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
            spotlight.style.zIndex = '9998';
            spotlight.style.pointerEvents = 'none';
            
            // Create a hole in the overlay around the failed element
            spotlight.style.boxShadow = `0 0 0 9999px rgba(0, 0, 0, 0.5)`;
            spotlight.style.clip = `rect(${rect.top}px, ${rect.right}px, ${rect.bottom}px, ${rect.left}px)`;
            
            document.body.appendChild(spotlight);
        }
    """, test_name, failed_step, failed_element if failed_element else None)

def find_relevant_element(driver, failed_step):
    """Find the most relevant element based on the failed step description."""
    try:
        # Try to find elements based on common patterns in step descriptions
        relevant_elements = driver.execute_script("""
            function findRelevantElements(stepText) {
                // Convert step text to lowercase for easier matching
                stepText = stepText.toLowerCase();
                
                // Array to store potential matches with their priority
                let matches = [];
                
                // Helper function to add elements with priority
                function addElements(elements, priority) {
                    elements.forEach(el => matches.push({element: el, priority: priority}));
                }
                
                // Find focused or active elements (highest priority)
                addElements([document.activeElement].filter(el => el && el.tagName !== 'BODY'), 10);
                
                // Find elements with error states
                addElements(
                    Array.from(document.querySelectorAll('.error, .invalid, [aria-invalid="true"], .has-error')),
                    9
                );
                
                // Find recently interacted elements
                addElements(
                    Array.from(document.querySelectorAll(':focus, :active, input:not([value=""]), select:not([value=""]), textarea:not(:empty)')),
                    8
                );
                
                // Find elements with matching text content
                document.querySelectorAll('*').forEach(el => {
                    let text = el.textContent.toLowerCase();
                    if (text && stepText.includes(text)) {
                        matches.push({element: el, priority: 7});
                    }
                });
                
                // Sort by priority and return the top element
                matches.sort((a, b) => b.priority - a.priority);
                return matches.length > 0 ? matches[0].element : null;
            }
            return findRelevantElements(arguments[0]);
        """, failed_step)
        
        return relevant_elements
    except Exception:
        return None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure with enhanced visualization and step tracking."""
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = item.funcargs.get("browser")

        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")

            try:
                # Get failed step information
                failed_step = None
                if call.excinfo:
                    if hasattr(call.excinfo.value, 'step_info'):
                        failed_step = call.excinfo.value.step_info
                    elif TestContext.current_step:
                        failed_step = TestContext.current_step

                # Find relevant element for the failed step
                relevant_element = None
                if failed_step:
                    relevant_element = find_relevant_element(driver, failed_step)

                # Track elements to highlight and their original styles
                elements_to_highlight = []
                original_styles = []

                if relevant_element:
                    elements_to_highlight.append(relevant_element)
                else:
                    # Fallback to finding recently interacted elements
                    active_element = driver.execute_script("return document.activeElement;")
                    if active_element and active_element.tag_name.lower() not in ["body", "html"]:
                        elements_to_highlight.append(active_element)

                # Highlight identified elements
                for element in elements_to_highlight:
                    try:
                        original_style = highlight_element(driver, element)
                        original_styles.append((element, original_style))
                    except WebDriverException:
                        continue

                # Add failure overlay with step information and spotlight effect
                add_failure_overlay(driver, item.name, failed_step, relevant_element)

                # Take screenshot
                driver.save_screenshot(screenshot_path)
                
                # Attach to Allure report
                allure.attach.file(
                    screenshot_path,
                    name=f"Failure-Screenshot-{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
                
                # Add failure context to Allure
                if failed_step:
                    allure.attach(
                        f"Failed Step: {failed_step}",
                        name="Failure Context",
                        attachment_type=allure.attachment_type.TEXT
                    )

                # Cleanup highlights and overlays
                for element, original_style in original_styles:
                    try:
                        driver.execute_script(
                            "arguments[0].setAttribute('style', arguments[1]);",
                            element,
                            original_style or ""
                        )
                    except WebDriverException:
                        continue

                # Remove overlay and spotlight
                driver.execute_script("""
                    document.querySelectorAll('#test-failure-overlay, div[style*="rgba(0, 0, 0, 0.5)"]').forEach(el => el.remove());
                """)

                print(f"🖼️ Enhanced failure screenshot saved: {screenshot_path}")
                if failed_step:
                    print(f"❌ Failed Step: {failed_step}")

            except Exception as e:
                allure.attach(
                    f"Screenshot enhancement failed: {str(e)}\n{str(e.__traceback__)}",
                    name="Screenshot Error",
                    attachment_type=allure.attachment_type.TEXT
                )
                print(f"⚠️ Screenshot enhancement failed: {str(e)}")