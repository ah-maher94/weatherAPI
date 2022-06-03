import requests

class Weather:

    API_Key = "84a4a974cf1f411d983205140220306"
    base_url = "https://api.weatherapi.com/v1/"
    

    @staticmethod
    def get_weather_data(city):
        weather_url = f'{Weather.base_url}current.json?key={Weather.API_Key}&q={city}&aqi=no'
        return requests.get(weather_url).json()


    @classmethod
    def get_current_temperature(self, city):
        weather_data = self.get_weather_data(city)
        print(f'Current temp: {weather_data["current"]["temp_c"]}')


    @classmethod
    def get_temperature_after(self, city, days, hour=None):
        weather_url = f'{Weather.base_url}forecast.json?key={Weather.API_Key}&q={city}&days={days}&aqi=no&alerts=no'
        weather_data = requests.get(weather_url).json()
        print(f'Temp after {days} days: {weather_data["current"]["temp_c"]}')


    @classmethod
    def get_lat_and_long(self, city):
        weather_data = self.get_weather_data(city)
        print(f'Lat: {weather_data["location"]["lat"]}, long: {weather_data["location"]["lon"]}')




def main():
    city = input('Enter city: ')
    days = int(input('Enter num of days: '))
    Weather.get_current_temperature(city)
    Weather.get_temperature_after(city, days)
    Weather.get_lat_and_long(city)

if __name__ == "__main__":
    main()