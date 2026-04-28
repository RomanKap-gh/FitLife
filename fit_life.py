# Проект FitLife - MVP версия 1.0


# 1. Знакомство с пользователем
# Запрос имени пользователя
def request_name():
    """
    Запрашивает имя пользователя

    Returns:
        str: имя пользователя
    """
    while True:
        user_name = input('Как Вас зовут? ').strip()
        if user_name == '':
            print('Ошибка! Вы забыли ввести буквы!\n')
        else:
            return user_name


# Запрос возраста пользователя
def request_age():
    """
    Запрашивает возраст пользователя

    Returns:
        int: возраст пользователя
    """
    MAX_AGE = 100
    MIN_AGE = 6
    while True:
        try:
            user_age = int(input('Сколько Вам лет? '))
        except ValueError:
            print('\nОшибка!!! Введите целое число\n')
        else:
            if user_age > MAX_AGE:
                print('Упс...перебор!! Введите корректное значение')
            elif user_age < MIN_AGE:
                print('Упс...недобор!! Введите корректное значение')
            else:
                return user_age


# 2. Сбор данных
# Запрос веса пользователя
def request_weight():
    """
    Запрашивает вес пользователя

    Returns:
        float: вес пользователя
    """
    MAX_WEIGHT = 150
    MIN_WEIGHT = 30
    while True:
        try:
            user_weight = float(input(
                'Введите свой вес в килограммах (например 60.5): '))
        except ValueError:
            print('\nОшибка!!! Неккоректный ввод данных!\n')
        else:
            if user_weight > MAX_WEIGHT:
                print('Упс...перебор!! Введите корректное значение')
            elif user_weight < MIN_WEIGHT:
                print('Упс...недобор!! Введите корректное значение')
            else:
                return user_weight


# Запрос роста пользователя
def request_height():
    """
    Запрашивает рост пользователя

    Returns:
        float: возраст пользователя
    """
    MAX_HEIGHT = 2.2
    MIN_HEIGHT = 1
    while True:
        try:
            user_height = float(input(
                'Введите свой рост в метрах (например 1.75): '))
        except ValueError:
            print('\nОшибка!!! Неккоректный ввод данных!\n')
        else:
            if user_height > MAX_HEIGHT:
                print('Упс...перебор!! Введите корректное значение')
            elif user_height < MIN_HEIGHT:
                print('Упс...недобор!! Введите корректное значение')
            else:
                return user_height


# 3. Логика расчетов
# Расчет индекса массы тела
def calculation_bmi(user_weight, user_height):
    """
    Рассчитывает индекс массы тела

    Args:
        user_weight (float): вес пользователя
        user_height (float): рост пользователя

    Returns:
        float: индекс массы тела
    """
    return round(user_weight / (user_height ** 2), 1)


# Расчет рекомендации нормы воды в день
def calculation_water_needed(user_weight):
    """
    Рассчитывает норму воды в день в литрах

    Args:
        user_weight (float): вес пользователя

    Returns:
        float: норма воды в день в литрах
    """
    ML_ON_KG = 30
    ML_IN_L = 1000
    return round(user_weight * ML_ON_KG / ML_IN_L, 1)


# 4. Вывод красивого результата
# Функция вывода отчета
def print_result(user_name, user_age, bmi, water_l):
    """
    Выводит параметры пользователя

    Args:
        user_name (str): имя пользователя
        user_age (int): возраст пользователя
        bmi (float): индекс массы тела пользователя
        water_l (float): норма воды в день в литрах
    """
    if (user_age // 10 == 1):
        year = 'лет'
    elif (user_age % 10 == 1):
        year = 'год'
    elif (0 < user_age % 10 < 5):
        year = 'года'
    else:
        year = 'лет'
    print(f'\nОтчет для пользователя:   {user_name} ({user_age} {year})')
    print(f'Твой Индекс Массы Тела:   {bmi}')
    print(f'Рекомендуемая норма воды: {water_l} л в день\n')
    print(f'Расчет окончен. {user_name}, будьте здоровы!')


print('Добрый день!')
user_name = request_name()
user_age = request_age()
print(f'\nПриятно с Вами познакомиться, {user_name}!')
print(
    'Я помогу вам рассчитать Индекс Массы Тела, а также дам '
    'рекомендации по норме употребляемой воды в литрах в день.')
print('Для подсчетов мне понадобятся ряд Ваших параметров.\n')
user_weight = request_weight()
user_height = request_height()
bmi = calculation_bmi(user_weight, user_height)
water_l = calculation_water_needed(user_weight)
print_result(user_name, user_age, bmi, water_l)
