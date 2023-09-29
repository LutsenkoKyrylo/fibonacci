def fib(n):
    fib_1 = [0, 1]  # Початкові числа Фібоначчі
    while len(fib_1) < n:
        num = fib_1[-1] + fib_1[-2]
        fib_1.append(num)
    return fib_1

# Кількість чисел Фібоначчі, які ви хочете згенерувати
n = int(input("Введіть кількість чисел Фібоначчі: "))
if n <= 0:
    print("Введіть додатне число.")
else:
    res= fib(n)
    print("Числа Фібоначчі:", res)