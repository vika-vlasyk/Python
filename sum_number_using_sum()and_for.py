def sum_numbers(*numbers):
    try:
        result = sum(number for number in numbers if number > 0)
    except TypeError:
        result = 0
    return result


if __name__ == "__main__":
    print(sum_numbers(5, 10, -5, 15))
