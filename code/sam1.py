from collections import Counter
import re
def count_words_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = re.findall(r'\b\w+\b', f.read().lower())
        word_count = Counter(words)
        most_common_word = word_count.most_common(1)[0]
    return len(words), most_common_word
total_words, most_common_word = count_words_in_file("code/test.txt")
print(f"Всего слов в файле: {total_words}")
print(f"Самое частое слово: '{most_common_word[0]}', количество вхождений: {most_common_word[1]}")