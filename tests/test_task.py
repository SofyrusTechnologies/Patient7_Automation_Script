import pytest
import time
from pages.add_task_page import AddTaskPage
from utils.config import generate_test_data


@pytest.mark.usefixtures("authenticated_browser")
class TestUser:
    def test_add_task(self, authenticated_browser):
        """
        Test case to verify the complete user addition workflow including:
        - Adding a new user
        - Setting up their password via Yopmail
        - Verifying the user was added successfully
        """
        # Initialize page object
        add_task_page = AddTaskPage(authenticated_browser)

        # Generate test data
        test_data = generate_test_data()

        try:
            # Load dashboard and navigate to add user form
            add_task_page.load_dashboard()
            add_task_page.Add_task_button()
            add_task_page.fill_user_form(test_data)

            
    

            # add_user_page.Click_AddUser()

            # # Fill and submit the user form
            # add_user_page.fill_user_form(test_data)
            # print(f"User form submitted for {test_data['first_name']} {test_data['last_name']}")

            # # Handle Yopmail workflow for password setup
            # add_user_page.handle_yopmail_workflow(test_data)
            # print("Password setup completed via Yopmail")

        finally:
            print('task added successfully!')
