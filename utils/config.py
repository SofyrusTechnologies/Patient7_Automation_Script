import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("en_US")

def generate_random_dob():
    """Generate a random date of birth between 18 and 90 years old."""
    start_date = datetime.today() - timedelta(days=90*365)
    end_date = datetime.today() - timedelta(days=18*365)
    random_dob = fake.date_between(start_date=start_date, end_date=end_date)
    return random_dob.strftime("%m/%d/%Y")  

def generate_test_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.user_name() + "@yopmail.com",
        "dob": generate_random_dob(),
        "address": fake.address(),
        "city": fake.city(),
        "state": fake.state(),
        "zip_code": fake.zipcode(),
        "mobile_no": "+1" + str(random.randint(1000000000, 9999999999))  
        
    }
