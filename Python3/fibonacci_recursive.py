def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def generate_fibonacci_sequence(length):
    fib_list = []
    for i in range(length):
        fib_list.append(fibonacci(i))
    return fib_list

print(generate_fibonacci_sequence(int(input())))
