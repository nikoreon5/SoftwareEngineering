import re
def get_forbidden_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().split()
    return words
def blur_sentence(sentence, forbidden_words):
    for word in forbidden_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)
    return sentence

forbidden_words = get_forbidden_words("code/input.txt")
sentence = input("Введите предложение для проверки: ")
blured_sentence = blur_sentence(sentence, forbidden_words)
print("Результат:", blured_sentence)