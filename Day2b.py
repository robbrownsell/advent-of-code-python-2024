from NumberInput2 import get_numbers


def main(): var = {
    print(read_input(get_numbers()))
}


def up_or_down(number1: int, number2: int):
    if number1 > number2:
        return "DOWN"
    elif number1 == number2:
        return "SAME"
    else:
        return "UP"


def row_is_level_safe(numbers_in_row):
    new_num_arr = []
    for index, number in enumerate(numbers_in_row):
        for index2, newnum in enumerate(numbers_in_row):
            if index2 != index:
                new_num_arr.append(newnum)
        if row_is_safe(new_num_arr):
            return True
        new_num_arr = []
    return False


def row_is_safe(numbers_in_row):
    direction = ""
    for index, number in enumerate(numbers_in_row):
        if index < (len(numbers_in_row) - 1):
            number_1 = int(numbers_in_row[index])
            number_2 = int(numbers_in_row[index + 1])
            if direction != up_or_down(number_1, number_2) and direction != "":
                return False
            direction = up_or_down(number_1, number_2)
            if number_1 == number_2:
                return False
            if abs(number_1 - number_2) > 3:
                return False
    return True


def read_input(input):
    rows = input.split("\n")
    safe_rows = 0
    for row in rows:
        print("on row ", row)
        numbers_in_row: [] = row.split(" ")
        if row_is_level_safe(numbers_in_row):
            safe_rows += 1
            print("safe ", safe_rows)
        else:
            print("unsafe")
    return safe_rows


if __name__ == '__main__':
    main()
