import re
def show_text_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines_count = len(lines)
        total_words = 0
        letter_count = 0
        for line in lines:
            total_words += len(line.split())
            letter_count += len(re.findall(r'[a-zA-Z]', line))
        print(f"Количество букв латинского алфавита: {letter_count}")
        print(f"Количество слов: {total_words}")
        print(f"Количество строк: {lines_count}")
show_text_stats("code/input.txt")