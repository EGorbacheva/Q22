"""Реализовать программу для подсчёта индекса массы тела человека. Пользователь
вводит рост и вес с клавиатуры. На выходе - ИМТ и пояснение к нему в зависимости
от попадания в тот или иной диапазон. Использовать обработку исключений."""


def num_input():
    height = float(input("Введите ваш рост (м.): "))
    weight = float(input("Введите ваш вес (кг.): "))
    if height <= 0 or weight <= 0:
        raise ValueError
    return calc(height, weight)


def calc(height, weight):
    bmi = weight / height ** 2
    if bmi < 16:
        result = "выраженный дефицит массы тела"
        return print_result(bmi, result)
    elif 16 < bmi < 18.5:
        result = "недостаточная (дефицит) масса тела"
        return print_result(bmi, result)
    elif 18.5 < bmi < 25:
        result = "норма"
        return print_result(bmi, result)
    elif 25 < bmi < 30:
        result = "избыточная масса тела (предожирение)"
        return print_result(bmi, result)
    elif 30 < bmi < 35:
        result = "ожирение первой степени"
        return print_result(bmi, result)
    elif 35 < bmi < 40:
        result = "ожирение второй степени"
        return print_result(bmi, result)
    elif bmi > 40:
        result = "ожирение третьей степени (морбидное)"
        return print_result(bmi, result)


def print_result(bmi, result):
    print(f"Ваш ИМТ: {bmi: .1f}. Это {result}.")


def execute():
    try:
        num_input()
    except ValueError:
        print("Данные введены некорректно, попробуйте ещё раз")
        return execute()


execute()
