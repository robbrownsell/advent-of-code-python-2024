from NumberInput2 import get_numbers


def main(): var = {
    print(read_input(get_numbers()))
}


# def row_is_safe(numbers_in_row):
#     total = 0
#     for index, number in enumerate(numbers_in_row):
#         if index < (len(numbers_in_row)-1):
#             number_1 = int(numbers_in_row[index])
#             number_2 = int(numbers_in_row[index+1])
#             total = total + (number_1 - number_2)
#     if total > 0:
#         return True
#     else: return False

def row_is_safe(numbers_in_row):
    for index, number in enumerate(numbers_in_row):
        if index < (len(numbers_in_row)-1):
            number_1 = int(numbers_in_row[index])
            number_2 = int(numbers_in_row[index+1])
            if abs(number_1-number_2) > 3:
                return False
    return True


def read_input(input):
    rows = input.split("\n")
    safe_rows = 0
    for row in rows:
        print("on row ", row)
        numbers_in_row:[] = row.split(" ")
        if row_is_safe(numbers_in_row):
            safe_rows += 1
    return safe_rows

if __name__ == '__main__':
    main()
