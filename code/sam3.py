from collections import Counter

def threeMostFrequentDigits(inp):
    result = {}
    frequencies = Counter(int(digit) for digit in inp)
    threeMostCommonDigits = frequencies.most_common(3)
    sortedDigits = sorted(threeMostCommonDigits)
    for digit, count in sortedDigits:
        result[digit] = count
    return result

case = "2381936192299991"
result = threeMostFrequentDigits(case)
print("Три самых частых числа и их количество:", result)