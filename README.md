# Weather App

A Django application that reports the weather using the OpenWeatherMap API. Users can type in a city to see the current weather conditions.

## Features

- Fetches current weather data from the OpenWeatherMap API
- Allows users to search for weather information by city
- Displays temperature, weather conditions, and other relevant data

## Installation

Clone the repository:
```sh
git clone https://github.com/adammspaulding/weather_app.git
cd weather_app

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install pipenv
pipenv install

Set up environment variables: Create a .env file in the root directory and add your OpenWeatherMap API key:

API_KEY=your_api_key_here

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Usage
Open your web browser and go to http://127.0.0.1:8000/.

Enter a city name in the search box and click "Search".

View the current weather conditions for the specified city.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
OpenWeatherMap API for providing the weather data.
Django for the web framework.
# weather_app
