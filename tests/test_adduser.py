import pytest
import time
# from pages.add_user_page import AddUserPage
# from pages.patient_list_page import PatientListPage
from pages.add_user_page import AddUserPage
from utils.config import generate_test_data

@pytest.mark.usefixtures("authenticated_browser")
class TestUser:
    def test_user(self, authenticated_browser):
        dashboard_page = AddUserPage(authenticated_browser)
        dashboard_page.load_dashboard()
        


        add_user_buttton = AddUserPage(authenticated_browser) 
        add_user_buttton.Click_AddUser()
        
        add_patient_page = AddUserPage(authenticated_browser)
        test_data = generate_test_data()
        add_patient_page.fill_user_form(test_data)
        print(f" Doctor {test_data['first_name']} {test_data['last_name']} added successfully!")

        time.sleep(3)  
