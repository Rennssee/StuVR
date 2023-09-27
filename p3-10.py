def factorial(n):
    if n < 2:
        return 1
    else:
        c = n * factorial(n - 1)
        return c


# n! / ((n - k)! · k!)
def number_of_groups(n, k):
    a = n - k
    res = factorial(n) / (factorial(a) * factorial(k))
    return int(res)


print(number_of_groups(50, 7))
