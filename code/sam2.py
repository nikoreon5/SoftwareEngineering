import os

def read_and_check_file(filename):
    print(f"\n--- Проверка файла: {filename} ---")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content:
            raise ValueError("файл пустой")
        else:
            print("Содержимое файла:")
            print("===================")
            print(content)
            print("===================")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except ValueError as e:
        print(f"Ошибка данных: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('Это данные для спортивного программирования!\nСтрока 2')

with open('empty.txt', 'w', encoding='utf-8') as f:
    f.write('')

read_and_check_file('data.txt')
read_and_check_file('empty.txt')
read_and_check_file('non_existent_file.txt')