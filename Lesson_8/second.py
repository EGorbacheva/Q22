"""Реализовать программу с функционалом калькулятора для операций над двумя числами.
Числа и операция вводятся пользователем с клавиатуры. Использовать обработку исключений."""


def num_input():
    num_1, action, num_2 = input("Что посчитать? ").split()
    num_1, num_2 = int(num_1), int(num_2)
    return calc(num_1, action, num_2)


def calc(num_1, action, num_2):
    if action == "/":
        result = num_1 / num_2
        return print_result(num_1, action, num_2, result)
    elif action == "*":
        result = num_1 * num_2
        return print_result(num_1, action, num_2, result)
    elif action == "-":
        result = num_1 - num_2
        return print_result(num_1, action, num_2, result)
    elif action == "+":
        result = num_1 + num_2
        return print_result(num_1, action, num_2, result)
    elif action == "%":
        result = num_1 % num_2
        return print_result(num_1, action, num_2, result)
    elif action == "//":
        result = num_1 // num_2
        return print_result(num_1, action, num_2, result)
    else:
        raise ValueError


def print_result(num_1, action, num_2, result):
    print(f"{num_1} {action} {num_2} = {result: .2f}")


def execute():
    try:
        num_input()
    except ZeroDivisionError:
        print("Делитель не может быть нулём, попробуйте ещё раз")
        return execute()
    except ValueError:
        print("Данные введены неверно, попробуйте ещё раз")
        return execute()


execute()
