def more(param, min_value):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > min_value:
                return number
            else:
                print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")


def less_more(param, min_value, max_value):
    while True:
        try:
            number = int(input(f"{param} "))
            if min_value < number < max_value:
                return number
            else:
                print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")

def integer(param):
    while True:
        try:
            return int(input(f"{param} "))

        except:
            print("Число введено неправильно.")
