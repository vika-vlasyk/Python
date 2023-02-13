# def sum_number(number):
#     num = 1
#     result = 0
#     while num < number + 1:
#         result = result + num
#         num = num + 1
#     return result
# if __name__ == "__main__":
#     print(sum_number(10))


# def sum_number(number):
#     result = 0
#     for num in range(number + 1):
#         result += num
#     return result
# if __name__ == "__main__":
#     print(sum_number(10))


# def sum_number(number):
#     return sum(range(number + 1))


# if __name__ == "__main__":
#     print(sum_number(10))


# def sum_number(number):
#     try:
#         result = sum(range(number + 1))
#     except TypeError:
#         result = 0
#     return result


# if __name__ == "__main__":
#     print(sum_number(10))


def sum_number(number):
    """(int) -> int
    number - це додатне ціле число.
    Повертає суму цілих чисел від нуля
    до number, інакше нуль.
    >>> sum_number(5)
    15
    >>> sum_number(5.3)
    0
    >>> sum_number(-5)
    0
    >>> sum_number("5")
    0
    """
    try:
        result = sum(range(number + 1))
    except TypeError:
        result = 0
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(sum_number(10))
