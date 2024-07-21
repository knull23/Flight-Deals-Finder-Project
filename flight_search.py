# https://test.api.amadeus.com/v1/security/oauth2/token/
import requests
import os
from dotenv import load_dotenv
load_dotenv()

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


class FlightSearch:
    def __init__(self):
        self._api_key = os.environ['DB_API_KEY']
        self._api_secret = os.environ['DB_API_SECRET']
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }

        response = requests.post(
            url=TOKEN_ENDPOINT,
            headers=headers,
            data=body
        )

        if response.status_code != 200:
            print(f"Failed to get token: {response.status_code} {response.text}")
            return None

        token_data = response.json()
        print(f"Your token is {token_data['access_token']}")
        print(f"Your token expires in {token_data['expires_in']} seconds")
        return token_data['access_token']

    def get_destination_code(self, city_name):
        if not self._token:
            print("No token available. Unable to proceed.")
            return None

        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )

        if response.status_code != 200:
            print(f"Status code: {response.status_code}. Error: {response.text}")
            return None

        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError) as e:
            print(f"Error: {e}. No airport code found for {city_name}.")
            return None

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        if not self._token:
            print("No token available. Unable to proceed.")
            return None

        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        try:
            response = requests.get(
                url=FLIGHT_ENDPOINT,
                headers=headers,
                params=query,
            )

            if response.status_code != 200:
                print(f"check_flights() response code: {response.status_code}")
                print("There was a problem with the flight search.\n"
                      "For details on status codes, check the API documentation:\n"
                      "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference")
                print("Response body:", response.text)
                return None

            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


