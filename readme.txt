# **WeatherApp**
## **What is WeatherApp?**

WeatherApp is a simple desktop weather widget built with Python and Kivy.

The application is designed to allow users to:

- Search for a location.
- Retrieve and display the location's current weather information.
- Save locations for later use.
- Reload a previously saved location.
- Refresh the weather information for an existing saved location.

Weather data is retrieved from the OpenWeather API using Python's requests library.

Saved location information is stored locally in the weather_data file using JSON. This demonstrates basic data persistence by allowing the application to save information and retrieve it during future sessions.
In a larger production application, this local storage could be replaced by a database or backend service where saved locations are associated with authenticated user accounts.

## **Current Limitation**

Locations must currently be submitted using the + button in the application. The Enter key is not currently bound to the location submission function.

## **What are the functions?**

Weather.py is used to hold various functions that handle the pulling, saving, and processing of weather information 
Run main.py to test widget 

## **Requirments and Installation:** 
This app makes use of the kivy library, Kivy strongly recommends a virtual enviroment and pip: 


### Create a fresh virtual enviroment: 
python -m venv .venv

### Activate: 
.venv\Scripts\activate

### Update pip: 
python -m pip install --upgrade pip

### Install the required dependencies: 
python -m pip install -r requirements.txt




