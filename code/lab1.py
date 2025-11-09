from functools import lru_cache
import time

start_time = time.time()
@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))
end_time = time.time()
print(f'Время выполнения: {end_time - start_time} секунд.')