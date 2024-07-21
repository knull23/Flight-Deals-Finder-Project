import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()


class DataManager:
    def __init__(self):
        self.username = os.environ['DB_USERNAME']
        self.password = os.environ['DB_PASSWORD']
        self.prices_endpoint = os.environ["DB_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["DB_USERS_ENDPOINT"]
        self.auth_basic = os.environ['DB_AUTH_BASIC']
        self.authorization = HTTPBasicAuth(self.username, self.password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=self.prices_endpoint,
            auth=self.authorization
        )
        data = response.json()

        # Debug: Print the response data to understand its structure
        print("Response data:", data)

        try:
            self.destination_data = data["prices"]
        except KeyError:
            print("Key 'prices' not found in the response.")
            self.destination_data = []  # Default to an empty list to prevent further errors
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self.authorization
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(
            url=self.users_endpoint,
            auth=self.authorization,
        )
        data = response.json()
        print("Customer Data Response:", data)

        try:
            self.customer_data = data["users"]
        except KeyError:
            print("Key 'users' not found in the response.")
            self.customer_data = []  # Default to an empty list to prevent further errors
        return self.customer_data
