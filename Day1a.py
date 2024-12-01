from NumberInput import get_numbers


def main(): {
    # column_one = [] = add_ordered_numbers(get_numbers(), 1)
    print(sum(get_number_differences()))
}


def get_number_differences():
    column_one = add_ordered_numbers(get_numbers(), 1)
    column_two = add_ordered_numbers(get_numbers(), 2)
    num_difference = []
    for indx in range(len(column_one)):
        col_one_num = column_one[indx]
        col_two_num = column_two[indx]
        if col_one_num > col_two_num:
            num_difference.append(col_one_num - col_two_num)
        else:
            num_difference.append(col_two_num - col_one_num)
    return num_difference


def add_ordered_numbers(numbers, column: int):
    new_numbers = numbers.split("\n")
    selected_numbers = []
    for number in new_numbers:
        number_for_column = number.strip().split("   ")[column - 1]
        selected_numbers.append(int(number_for_column))

    return sorted(selected_numbers)


if __name__ == '__main__':
    main()
