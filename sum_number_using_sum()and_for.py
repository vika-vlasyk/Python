def sum_numbers(*numbers):
    return sum(number for number in numbers if number > 0)


if __name__ == "__main__":
    print(sum_numbers(5, 10, -5, 15))
