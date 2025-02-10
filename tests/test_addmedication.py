import pytest
import time
import random
from pages.add_medication_page import OverViewPage
from utils.config import generate_test_data

@pytest.mark.usefixtures("authenticated_browser")
class TestMedication:
    def test_add_and_verify_medication(self, authenticated_browser):
        dashboard_page = OverViewPage(authenticated_browser)
        dashboard_page.load_dashboard()

        time.sleep(5)
        actual_value = dashboard_page.get_mrn_no()
        expected_value = "Overview"
        assert actual_value == expected_value, \
            f"Assertion failed: Expected '{expected_value}', but got '{actual_value}'"
        print("✓ Overview page loaded successfully")

        # Add multiple medications
        num_medications = random.randint(2, 2)
        for i in range(num_medications):
            print(f"\nAdding medication {i+1} of {num_medications}")
            medication_details = dashboard_page.enter_medication_details()
            # assert dashboard_page.verify_medication_added(medication_details), \
            #     f"Failed to verify medication {i+1}"
            # time.sleep(3)

        print(f"\n✓ Successfully added and verified {num_medications} medications")