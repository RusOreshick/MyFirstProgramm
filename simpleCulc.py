while True:

    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
    operant = input("Введите операцию (+, -, *, /) или 0 для выхода: ")

    if operant == '0':
        break

    if operant == '+':
        print(f"Результат: {number1 + number2}")
    elif operant == '-':
        print(f"Результат: {number1 - number2}")
    elif operant == '*':
        print(f"Результат: {number1 * number2}")
    elif operant == '/':
        if number2 == 0:
            print("Ошибка: деление на ноль!")
        else:
            print(f"Результат: {number1 / number2}")
    else:
        print("Неверная операция")
    
    print()
print("Программа завершена")