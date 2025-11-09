import datetime

class Logger:
    def __init__(self, level='INFO'):
        self.level = level
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] LOGGER INIT: Декоратор готов к логированию на уровне {self.level}.")

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"[{self.level}] {timestamp} -> FUNCTION CALL: {func.__name__} | Args: {args}, Kwargs: {kwargs}"
            print(log_message)
            result = func(*args, **kwargs)
            log_message = f"[{self.level}] {timestamp} <- FUNCTION EXIT: {func.__name__} | Returned: {result}"
            print(log_message)
            return result
        return wrapper

@Logger(level='DEBUG')
def calculate_area(width, height):
    """Вычисляет площадь прямоугольника."""
    return width * height

@Logger(level='INFO')
def greet_user(name):
    """Формирует приветственное сообщение."""
    message = f"Привет, {name}! Добро пожаловать на сайт."
    return message

print("\n--- Запуск программы ---\n")
area = calculate_area(10, 5)
print(f"Результат вычисления площади: {area}")
print("-" * 20)
greeting = greet_user("Илья")
print(f"Результат приветствия: {greeting}")