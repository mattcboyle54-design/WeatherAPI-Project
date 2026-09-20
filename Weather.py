import requests
import json
import os


def get_file():
    """
    pulls information from the weather_data file and organizes it to be displayed on the app. 
    makes use of the os library and json library to acess and handle jsons files 

    returns:
    fill(list) a list of weather data to be added to the widget 
    """
    directory = 'weather_data'
    fill = []
    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)  
        return fill
    else: 
        #loads json in a list of dictonaries 
        for items in os.listdir(directory):
                with open(os.path.join(directory, items), 'r') as f:
                    data = json.load(f)
                    fill.append({'location': data['name'], 
                                 'weather': data['weather'][0]['description'],
                                 'temp': data['main']['temp'],
                                 'temp_min': data['main']['temp_min'],
                                 'temp_max': data['main']['temp_max']
                                 })
        
        return fill
           
    
def get_weather(api_key, city):
    """
    pulls weather information from the openweather api using city location using requests and link
    city(string): location of a city
    api_key(String): api_key used to access information

    returns:
    data(object) holds json data
    """
    #pulls data from api
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    #if sucessfull load into data else fail 
    if response.status_code == 200:
        data = response.json()
        return data  # Return the entire data for storage
    else:
        print("ERROR GET_WEATHER UNSUCESSFUL")
        return None
    


def save_data(city, data):
    """
    takes data from a json file and saved city location to upload json file into a weather_data directory. 
    If  directory doesn't exist it is made

    Inputs: 
    city(string): location of a city 
    data(object): holds json data 

    """
    
    directory = "weather_data"  # Define the directory name
    filename = f"{city.replace(' ', '_').lower()}.json"  # Create a filename from the city name
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it does not exist

    with open(os.path.join(directory, filename), 'w') as f:
        json.dump(data, f, indent=4)  # Write data to a file in JSON format

if __name__ == "__main__":
    print("NO TEST CODE DESIGNED")

 
