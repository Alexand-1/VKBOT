#vk1.a.lO7xbVVs2JEArJYVPjLsdPtcmAN2OJzzz6f48XyP4A74up4MhhXTvogLYKLbLEZ0xuR_8PePhuiXetuzdGh-F2iX3AAKFVmCWtp5ZhXCKG_SG2GmKj_YTmoH7RBoy5NNscBfPjloVzrUxjXj5ejgq_GaznnyBB7_ImdlBtxjtwG4WN65R_-8PN007M9CE_EoQyRpyx40TrV34vONnAz6iA

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import json
from ParserMoney import Currency
from WeatherParser import weather_check
from WeatherParsNextDay import weather_check_next_day

vk_session = vk_api.VkApi(token='vk1.a.lO7xbVVs2JEArJYVPjLsdPtcmAN2OJzzz6f48XyP4A74up4MhhXTvogLYKLbLEZ0xuR_8PePhuiXetuzdGh-F2iX3AAKFVmCWtp5ZhXCKG_SG2GmKj_YTmoH7RBoy5NNscBfPjloVzrUxjXj5ejgq_GaznnyBB7_ImdlBtxjtwG4WN65R_-8PN007M9CE_EoQyRpyx40TrV34vONnAz6iA')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)


user_status = {}  # Словарь для отслеживания статусов пользователей
user_cities = {}  # Словарь для сохранения городов пользователей
user_weather_city = {}




def send_keyboard(user_id, message, keyboard):
    vk_session.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'keyboard': keyboard,
        'random_id': 0,
    })

def create_start_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{"action": {"type": "text", "label": "Начать"}, "color": "primary"}]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)

def create_input_city_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{"action": {"type": "text", "label": "Назад"}, "color": "default"}]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)

def create_main_menu_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{"action": {"type": "text", "label": "Погода"}, "color": "primary"},
             {"action": {"type": "text", "label": "Афиша"}, "color": "primary"}],
            [{"action": {"type": "text", "label": "Валюта"}, "color": "primary"},
             {"action": {"type": "text", "label": "Пробка"}, "color": "primary"}]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)

def create_weather_menu_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{"action": {"type": "text", "label": "Погода на сегодня"}, "color": "primary"},
             {"action": {"type": "text", "label": "Погода на завтра"}, "color": "primary"}],
            [{"action": {"type": "text", "label": "Назад"}, "color": "default"}]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)

def create_afisha_menu_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{"action": {"type": "text", "label": "Афиша на сегодня"}, "color": "primary"},
             {"action": {"type": "text", "label": "Афиша на завтра"}, "color": "primary"}],
            [{"action": {"type": "text", "label": "Назад"}, "color": "default"}]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            user_id = event.user_id

            if msg == 'начать' or user_status.get(user_id) == 'start':
                user_status[user_id] = 'start'
                start_keyboard = create_start_keyboard()
                send_keyboard(user_id, 'Привет! Давай начнем.', start_keyboard)
                user_status[user_id] = 'waiting_for_city'
                input_city_keyboard = create_input_city_keyboard()
                send_keyboard(user_id, 'Введите свой город:', input_city_keyboard)
            elif user_status.get(user_id) == 'waiting_for_city':
                # Здесь вы можете добавить логику для обработки введенного города пользователем
                # В данном примере просто сохраняем город и сообщаем об успешной регистрации
                user_status[user_id] = 'main_menu'
                user_cities[user_id] = msg  # Просто сохраняем введенный город
                user_weather_city[user_id] = msg
                main_menu_keyboard = create_main_menu_keyboard()
                send_keyboard(user_id, f'Город {msg} успешно зарегистрирован!', main_menu_keyboard)

            elif user_status.get(user_id) == 'main_menu':
                if msg == 'погода':
                    user_status[user_id] = 'weather_menu'
                    weather_menu_keyboard = create_weather_menu_keyboard()
                    send_keyboard(user_id, 'Выберите день:', weather_menu_keyboard)
                elif msg == 'афиша':
                    user_status[user_id] = 'afisha_menu'
                    afisha_menu_keyboard = create_afisha_menu_keyboard()
                    send_keyboard(user_id, 'Выберите день:', afisha_menu_keyboard)
                elif user_status.get(user_id) == 'main_menu':
                    if msg == 'погода':
                        user_status[user_id] = 'weather_menu'
                        weather_menu_keyboard = create_weather_menu_keyboard()
                        send_keyboard(user_id, 'Выберите день:', weather_menu_keyboard)
                    elif msg == 'афиша':
                        user_status[user_id] = 'afisha_menu'
                        afisha_menu_keyboard = create_afisha_menu_keyboard()
                        send_keyboard(user_id, 'Выберите день:', afisha_menu_keyboard)
                    elif msg == 'валюта':
                        currency = Currency()
                        currency_prices = currency.get_all_currency_prices()
                        response_text = "Курсы валют:\n"
                        for currency_name,price in currency_prices.items():
                            response_text += f"{currency_name}:{price}\n"  # Замените на реальные данные
                        send_keyboard(user_id,response_text, create_main_menu_keyboard())
                    elif msg == 'пробка':
                        # Логика для кнопки "Пробка"
                        city = user_cities.get(user_id)
                        traffic_info = f"Пробки в городе {city}: 8.9 баллов"  # Замените на реальные данные
                        send_keyboard(user_id, traffic_info, create_main_menu_keyboard())
                # Добавьте логику для остальных пунктов меню (пробка, валюта)
                # ...
            elif user_status.get(user_id) == 'weather_menu':
                if msg == 'погода на сегодня':
                    city = user_cities.get(user_id)
                    if city:
                        # Ваш код для получения погоды на сегодня в указанном городе
                        # Вместо "Погода на сегодня в Москве: 25°C" используйте реальные данные
                        #weather_today = f"Погода на сегодня в {city}: 25°C"
                        #send_keyboard(user_id, weather_today, create_weather_menu_keyboard())
                        result = weather_check(city)
                        send_keyboard(user_id, result, create_weather_menu_keyboard())
                    else:
                        send_keyboard(user_id, "Город не найден. Введите свой город:", create_input_city_keyboard())
                elif msg == 'погода на завтра':
                    city = user_cities.get(user_id)
                    if city:
                        # Ваш код для получения погоды на завтра в указанном городе
                        # Вместо "Погода на завтра в Москве: 23°C" используйте реальные данные
                        result_next = weather_check_next_day(city)
                        send_keyboard(user_id, result_next, create_weather_menu_keyboard())
                    else:
                        send_keyboard(user_id, "Город не найден. Введите свой город:", create_input_city_keyboard())
                elif msg == 'назад':
                    user_status[user_id] = 'main_menu'
                    send_keyboard(user_id, 'Главное меню', create_main_menu_keyboard())
            elif user_status.get(user_id) == 'afisha_menu':
                if msg == 'афиша на сегодня':
                    # Ваш код для получения афиши на сегодня
                    afisha_today = "Афиша на сегодня: 12345"  # Замените на реальные данные
                    send_keyboard(user_id, afisha_today, create_afisha_menu_keyboard())
                elif msg == 'афиша на завтра':
                    # Ваш код для получения афиши на завтра
                    afisha_tomorrow = "Афиша на завтра: 34565"  # Замените на реальные данные
                    send_keyboard(user_id, afisha_tomorrow, create_afisha_menu_keyboard())
                elif msg == 'назад':
                    user_status[user_id] = 'main_menu'
                    send_keyboard(user_id, 'Главное меню', create_main_menu_keyboard())