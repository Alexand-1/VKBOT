import requests


def get_traffic_info(city):
    # Задаем URL для запроса к API Яндекс.Карт
    url = f'https://api-maps.yandex.ru/services/traffic-info/v1/actual?apikey=YOUR_API_KEY&format=json&geoid={city}'

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()

        # Извлекаем информацию о пробках (например, общий балл пробок)
        traffic_info = data.get('info', {}).get('stats', {}).get('jams', {}).get('totalScore', 'Информация не найдена')

        return traffic_info
    else:
        return f"Не удалось получить информацию о пробках в городе {city}"


# Пример использования
city = input("Введите название города (на английском): ")
traffic_info = get_traffic_info(city)
print(f"Пробки в городе {city}: {traffic_info}")