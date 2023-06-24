import time

import CheckNumbers

import json


def withdraw(sum):
    MIN_COMMISSION = 30
    MAX_COMMISSION = 600
    print("Снятие доступно при сумме на счёте не менее 80 у.е.")
    if 0 <= sum < 80:
        print("Вы не можете снять наличные.")
        return sum
    else:
        print("КОМИССИЯ ЗА СНЯТИЕ 1.5%, НО НЕ МЕНЕЕ 30 И НЕ БОЛЕЕ 600 У.Е.")
        while True:
            answer = CheckNumbers.more("""Введите сумму, кратную 50 у.е.
Для выхода в меню введите 0:""", -1)
            if answer == 0:
                return sum
            if answer > sum:
                print("Вы ввели сумму, превышающую доступный лимит.")
            elif answer % 50 != 0:
                print("Вы ввели сумму, не кратную 50 у.е.")
            else:
                commission = 0.015 * answer
                if commission < MIN_COMMISSION:
                    answer += MIN_COMMISSION
                elif commission > MAX_COMMISSION:
                    answer += MAX_COMMISSION
                else:
                    answer *= 1.015
                if answer > sum:
                    print("Превышен лимит снятия.")
                    return sum
                else:
                    sum -= answer
                    print(f"\nВаш баланс: {sum:.2f} у.е.")
                    return sum


def deposit(sum):
    while True:
        answer = CheckNumbers.more("""Введите сумму, которую желаете внести, кратную 50 у.е.
Для выхода в меню введите 0:""", -1)
        if answer == 0:
            return sum
        if answer % 50 == 0:
            sum += answer
            print(f"\nВаш баланс: {sum:.2f} у.е.")
            return sum
        else:
            print("Вы ввели сумму, не кратную 50 у.е.")
            continue


def read_data():
    with open('operations.txt') as json_file:
        return json.load(json_file)


def save_data(data):
    with open('operations.txt', 'w') as json_file:
        json.dump(data, json_file)


def print_history(data):
    if len(data) == 0:
        print("Ваша история операций пуста.")
    else:
        for i in data:
            print(f"Операция: {i[0]}, Сумма операции: {i[1]:.2f} у.е., Баланс: {i[2]:.2f} у.е.")


data = read_data()
if len(data) == 0:
    sum = 0
else:
    sum = data[-1][2]
print(f"\nВаш баланс: {sum:.2f} у.е.")
while True:
    count = len(data)
    time.sleep(1)
    sum_old = sum
    if sum > 5_000_000:
        sum *= 0.9
        data.append(["wealth tax", -0.1 * sum_old, sum])
        save_data(data)
        print(f"""\nВаш баланс превышает 5 000 000 у.е., поэтому был списан налог на богатство 10%.
Ваш баланс: {sum:.2f} у.е.""")
    if count > 0 and count % 3 == 0:
        sum *= 1.03
        data.append(["interest on balance", 0.03 * sum_old, sum])
        save_data(data)
        print(f"""\nПоздравляем! Это у Вас {count}-я операция!
Вам начислены 3% от остатка на балансе.
\nВаш баланс: {sum:.2f} у.е.""")
    print("""\nВ банкомате доступно 3 операции:

1. Снятие наличных;
2. Внесение наличных;
3. Просмотр лога;
4. Выход.\n""")
    selection = CheckNumbers.less_more("Введите номер операции:", 0, 4)
    if selection == 1:
        sum = withdraw(sum)
        if sum != sum_old:
            data.append(["withdraw", sum_old - sum, sum])
            save_data(data)
    elif selection == 2:
        sum = deposit(sum)
        if sum != sum_old:
            data.append(["deposit", sum - sum_old, sum])
            save_data(data)
    elif selection == 3:
        print_history(data)
    else:
        print("Выход...")
        break
