def sum_number(number):
    num = 1
    result = 0
    while num < number + 1:
        result = result + num
        num = num + 1
    return result
if __name__ == "__main__":
    print(sum_number(10))
