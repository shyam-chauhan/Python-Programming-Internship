import requests

API_key = '01234567890'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'
    res = requests.get(url).json()
    return res


def main():
    city = input("Enter city name to fetch weather info. : ")
    data = get_weather(city)
    print(f"Weather in {city}")
    print(f"Temperature: {data['main']['temp']} °C")


if __name__ == '__main__':
    main()