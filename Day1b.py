from NumberInput import get_numbers


def main(): {
    # column_one = [] = add_ordered_numbers(get_numbers(), 1)
    print(sum(get_number_similarities()))
}


def get_number_similarities():
    column_one = add_ordered_numbers(get_numbers(), 1)
    column_two = add_ordered_numbers(get_numbers(), 2)
    similarities_arr = []
    for num_one in column_one:
        number_of_similarities = 0
        for num_two in column_two:
            if num_two == num_one:
                number_of_similarities = number_of_similarities+1
        similarities_arr.append(num_one*number_of_similarities)
    return similarities_arr


def add_ordered_numbers(numbers, column: int):
    new_numbers = numbers.split("\n")
    selected_numbers = []
    for number in new_numbers:
        number_for_column = number.strip().split("   ")[column - 1]
        selected_numbers.append(int(number_for_column))

    return sorted(selected_numbers)


if __name__ == '__main__':
    main()
