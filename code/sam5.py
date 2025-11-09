class InvalidCredentialsError(Exception):
    """
    Собственное исключение, вызываемое при недопустимых 
    учетных данных (логине/пароле), например, если они слишком короткие.
    """
    def __init__(self, message="Недопустимые учетные данные. Проверьте длину логина и пароля."):
        self.message = message
        super().__init__(self.message)

def check_username(username):
    """Проверяет, что логин имеет длину не менее 5 символов."""
    print(f"\n--- Проверка логина: '{username}' ---")
    if len(username) < 5:
        raise InvalidCredentialsError(f"Логин '{username}' слишком короткий. Минимальная длина - 5 символов.")
    else:
        print("Логин прошел проверку.")
        
def check_password(password):
    """Проверяет, что пароль не является стандартным '12345'."""
    print(f"\n--- Проверка пароля ---")
    if password == '12345':
        raise InvalidCredentialsError("Пароль '12345' является небезопасным. Выберите другой.")
    else:
        print("Пароль прошел проверку.")

try:
    check_username("Nikolay")
    check_password("SecureP@ss123")
except InvalidCredentialsError as e:
    print(f"!!! ОШИБКА АВТОРИЗАЦИИ: {e}")

print("\n" + "=" * 30)

try:
    check_username("nk") # слишком короткий пароль
    check_password("ValidPassword")
except InvalidCredentialsError as e:
    print(f"!!! ОШИБКА АВТОРИЗАЦИИ: {e}")

print("\n" + "=" * 30)

try:
    check_username("Vladimir")
    check_password("12345") # небезопасный пароль
except InvalidCredentialsError as e:
    print(f"!!! ОШИБКА АВТОРИЗАЦИИ: {e}")