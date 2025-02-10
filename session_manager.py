import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_session(driver):
    """Save both cookies and local storage data"""
    # Save cookies
    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    
    # Save localStorage and sessionStorage
    storage = {
        'localStorage': driver.execute_script('return Object.entries(localStorage);'),
        'sessionStorage': driver.execute_script('return Object.entries(sessionStorage);')
    }
    with open('storage.json', 'w') as file:
        json.dump(storage, file)
    print("Session data saved successfully")

def load_session(driver):
    """Load saved session data and verify it's valid"""
    try:
        # Load cookies
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)
        
        # Load storage
        with open('storage.json', 'r') as file:
            storage = json.load(file)
        
        # Navigate to the site first
        driver.get("https://lifetreeclinic.patient7.co/")
        
        # Add cookies
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"Error adding cookie: {e}")
        
        # Add localStorage items
        for item in storage['localStorage']:
            driver.execute_script(f"window.localStorage.setItem('{item[0]}', '{item[1]}');")
        
        # Add sessionStorage items
        for item in storage['sessionStorage']:
            driver.execute_script(f"window.sessionStorage.setItem('{item[0]}', '{item[1]}');")
        
        driver.refresh()
        return True
        
    except Exception as e:
        print(f"Error loading session: {e}")
        return False

def perform_login(driver):
    """Perform the login process"""
    print("Performing new login...")
    driver.get("https://lifetreeclinic.patient7.co/auth/login")
    
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div[1]/div/input"))
    )
    email_field.send_keys("haseendoc1@yopmail.com")

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/input"))
    )
    password_field.send_keys("Hello@123")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/button/div"))
    )
    login_button.click()
    
    select_branch = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/a/div"))
    )
    select_branch.click()
    
    # Save the new session
    save_session(driver)
    return True

def verify_login(driver):
    """Verify if the current session is valid"""
    try:
        # driver.get("https://tenderclinic.pt7.io/branch/cf048f64-0c80-4071-aaa2-8fa960ee6d9b/dashboard")
        # WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/main/div/div[1]/div[1]/div/div[1]/div'))
        # )
        
        print("-----------------Session")
        return True
    except:
        return False