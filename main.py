print('Choose an option:')
print('1-Print a sequence to N')
print('2-Print Nth term')
ans = int(input())


def fibonacci(n):
    if n in fibonacci_dict:
        return fibonacci_dict[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1)+fibonacci(n-2)

    fibonacci_dict[n] = value
    return value


fibonacci_dict = {}
if ans == 1:
    print('Sequence Limit=?')
    lim = int(input())
    for n in range(1, lim+1):
        fibonacci(n)
        print(n, ":", fibonacci(n))
elif ans == 2:
    print('Nth term = ?')
    lim = int(input())
    for n in range(1, lim+1):
        fibonacci(n)
    print(lim, ":", fibonacci(lim))
else:
    print('Option not valid.')
