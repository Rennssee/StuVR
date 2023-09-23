result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand = float(input("Введіть число: "))

            if result is None:
                result = operand
            else:
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "*":
                    result *= operand
                elif operator == "/":
                    if operand == 0:
                        print("Помилка: ділення на нуль.")
                        break
                    result /= operand
            operator = None  # Очищаємо оператор після використання
            wait_for_number = False

        except ValueError:
            print("Будь ласка, введіть коректне число.")
            continue
    else:
        operator = input(">>>")

        if operator in ["+", "-", "*", "/"]:
            wait_for_number = True
        elif operator == "=":
            print(f"Результат: {result}")
            break
        else:
            print("Некоректний оператор. Будь ласка, спробуйте ще раз.")
