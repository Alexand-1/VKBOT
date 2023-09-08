import requests
from bs4 import BeautifulSoup


def weather_check_next_day(city):
    url = f'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+{city}+завтра'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    weather = soup.select('#wob_tm')[0].getText().strip()

    return f'Температура воздуха в городе {city} завтра: {weather} C'

