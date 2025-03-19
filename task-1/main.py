def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return n
        elif cache.get(n):
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci

func = caching_fibonacci()

print(func(10))
print(func(15))
