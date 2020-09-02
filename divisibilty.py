def divisibility_by_3(number: int) -> bool:
    """

    :type number: int
    """
    return sum(list(map(int, list(str(number))))) % 3 == 0  # if true then divisble


def divisibility_by_5(number: int) -> bool:
    """

    :type number: int
    """
    return list(map(int, list(str(number))))[-1] == 5  # if true then divisible


def divisibility_by_7(number: int) -> bool:
    """

    :type number: int
    """
    num = list(map(int, list(str(number))))
    num1 = int("".join(list(map(str, num[:-1]))))
    num2 = int(num[-1])
    return ((num1 - (num2 * 2)) % 7) == 0  # if true then divisible
