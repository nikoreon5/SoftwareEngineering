def add_two_and_input(user_input):
    print(f"\n--- Тест: Ввод '{user_input}' (тип: {type(user_input).__name__}) ---")
    try:
        number = int(user_input) 
        result = 2 + number
        print(f"Успешно: 2 + {number} = {result}")
    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

add_two_and_input("5")
add_two_and_input("-10")
add_two_and_input("Привет")
add_two_and_input("3.14")