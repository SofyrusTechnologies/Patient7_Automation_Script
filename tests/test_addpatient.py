import pytest
import time
from pages.dashboard_page import DashboardPage
from pages.patient_list_page import PatientListPage
from pages.add_patient_page import AddPatientPage
from utils.config import generate_test_data

@pytest.mark.usefixtures("authenticated_browser")
class TestDashboard:
    def test_dashboard_welcome_message(self, authenticated_browser):
        dashboard_page = DashboardPage(authenticated_browser)
        dashboard_page.load_dashboard()

        # Assert welcome message
        actual_value = dashboard_page.get_welcome_message()
        expected_value = "Welcome back"
        assert actual_value == expected_value, f"Assertion failed: Expected '{expected_value}', but got '{actual_value}'"
        print("✅ Assertion Passed: Welcome back message verified")

        # Navigate to Patient List
        dashboard_page.navigate_to_patient_list()
        
        # Verify Patient List Loaded
        patient_list_page = PatientListPage(authenticated_browser)
        actual_value = patient_list_page.verify_patient_list_loaded()
        expected_value = "Color Tag"
        assert actual_value == expected_value, f"Assertion failed: Expected '{expected_value}', but got '{actual_value}'"
        print("✅ Assertion Passed: Patient List loaded successfully")

        # Add Patient
        patient_list_page.click_add_patient()
        add_patient_page = AddPatientPage(authenticated_browser)
        test_data = generate_test_data()
        add_patient_page.fill_patient_form(test_data)
        print(f"✅ Patient {test_data['first_name']} {test_data['last_name']} added successfully!")

        time.sleep(3)  # Allow time for form submission
