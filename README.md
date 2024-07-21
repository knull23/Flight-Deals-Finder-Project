Flight Deals Finder
- Flight Deals Finder is a Python project designed to find and notify you about the cheapest flights from a specified origin airport to various destinations. 
- The project integrates with multiple APIs to fetch flight data, update destination information, and send notifications via SMS and email.

## Features
1. Fetch Flight Data: Searches for the cheapest flights to specified destinations using the Amadeus API.
2. Update Destination Information: Updates destination airport codes using the Amadeus API.
3. Notifications: Sends notifications about cheap flights via SMS using Twilio and email using SMTP.
4. Rate Limiting Handling: Includes delays in API requests to handle rate limiting.

## Project Structure
.
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── .env
└── README.md

- main.py
The main script that orchestrates the flight search and notification process.

- data_manager.py
Handles fetching and updating destination and user data from the Google Sheets API via Sheety.

- flight_search.py
Integrates with the Amadeus API to fetch flight information and airport codes.

- flight_data.py
Contains the FlightData class and a helper function find_cheapest_flight to process flight data.

- notification_manager.py
Handles sending notifications via SMS using Twilio and emails using SMTP.

## Setup and Installation
Prerequisites
Python 3.7+
Virtual environment (recommended)

## Installation
- Clone the repository:
  git clone https://github.com/your-username/flight-deals-finder.git
  cd flight-deals-finder

- Create a virtual environment and activate it:
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

- Install the required packages:
  pip install -r requirements.txt

- Create a .env file in the project root and add your API keys and credentials:
DB_API_KEY="your_amadeus_api_key"
DB_API_SECRET="your_amadeus_api_secret"
DB_USERNAME="your_sheety_username"
DB_PASSWORD="your_sheety_password"
DB_AUTH_BASIC="your_basic_auth_token"
DB_ACC_SID="your_twilio_account_sid"
DB_AUTH_TOKEN="your_twilio_auth_token"
DB_TWILIO_PHONE_NO="your_twilio_phone_number"
DB_YOUR_PHONE_NUMBER="your_phone_number"
DB_WHATSAPP_NUMBER="your_whatsapp_number"
DB_PRICES_ENDPOINT="your_sheety_prices_endpoint"
DB_USERS_ENDPOINT="your_sheety_users_endpoint"
DB_MY_EMAIL="your_email_address"
DB_MY_PASSWORD="your_email_password"
DB_EMAIL_PROVIDER_SMTP_ADDRESS="smtp.your_email_provider.com"

- Run the script:
  python main.py

## Usage
1. Ensure your .env file is correctly configured with all the required API keys and endpoints.
2. Run main.py to start the flight search and notification process.
3. The script will fetch flight data, update destination codes, and notify you via SMS and email about the cheapest flights.

## API References
- Amadeus API
- Sheety API
- Twilio API

## Contributing
- Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
