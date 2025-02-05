import pytest
from pages.main_dashboard_page import DashboardPage

@pytest.mark.usefixtures("authenticated_browser")
class TestDashboard:
    def test_dashboard_elements(self, authenticated_browser):
        """Test to verify various elements on the dashboard."""
        dashboard = DashboardPage(authenticated_browser)
        dashboard.open_dashboard()
        
        print(dashboard.get_text(dashboard.WELCOME_MESSAGE))

        # Assertion for Welcome Message
        assert dashboard.get_text(dashboard.WELCOME_MESSAGE) == "Welcome back", "Welcome message mismatch"

        # Assertion for Today's Top Consults
        assert dashboard.get_text(dashboard.TODAY_TOP_CONSULTS) == "Today’s Top Consults", "Top Consults mismatch"
        
        print(dashboard.get_text(dashboard.TODAY_TOP_CONSULTS))

        # Assertion for Today's Schedule
        assert dashboard.get_text(dashboard.TODAY_SCHEDULE) == "Today's Schedule", "Today's Schedule mismatch"
        
        print(dashboard.get_text(dashboard.TODAY_SCHEDULE))

        # Assertion for Monthly Finances
        assert dashboard.get_text(dashboard.MONTHLY_FINANCES) == "Monthly Finances", "Monthly Finances mismatch"
        print(dashboard.get_text(dashboard.MONTHLY_FINANCES))


        # Assertion for Tasks
        assert dashboard.get_text(dashboard.TASKS) == "Tasks", "Tasks mismatch"
        print(dashboard.get_text(dashboard.TASKS))

