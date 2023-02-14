# def sum_numbers(*numbers):
#     num = 0
#     result = 0
#     while num < len(numbers):
#         if numbers[num] > 0:
#             result = result + numbers[num]
#         num = num + 1
#     return result


# if __name__ == "__main__":
#     print(sum_numbers(5, 10, -5, 15))


def sum_numbers(*numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += number
    return result


if __name__ == "__main__":
    print(sum_numbers(5, 10, -5, 15))
