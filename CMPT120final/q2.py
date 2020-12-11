from functools import reduce


def odd_even_max_while(nums):
    cont = True
    i = 0
    odd = 0
    even = 0
    while cont and (i < len(nums)):
        if nums[i] % 2 == 0:
            even += nums[i]
            i += 1
        else:
            odd += nums[i]
            i += 1
    if odd > even:
        return odd
    else:
        return even


def odd_even_max_for(nums):
    odd = 0
    even = 0

    for i in nums:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    if odd > even:
        return odd
    else:
        return even


def even(list):
    """
    returns all the even numbers in a list
    :param list: list of integer values
    :return: list of even integer values
    """
    return list % 2 == 0


def odd(list):
    """
    returns all the odd numbers in a list
    :param list: list of integer values
    :return: list of odd integer values
    """
    return list % 2 == 1


def add(x, y):
    return x + y


def compare(x, y):
    return x > y


def odd_even_max_noloops(nums):
    evenNums = filter(even, nums)
    oddNums = filter(odd, nums)

    oddSum = reduce(add, oddNums)
    evenSum = reduce(add, evenNums)

    sumsList = [evenSum, oddSum]
    map_object = map(compare, sumsList)

    if map_object:
        return oddSum
    else:
        return evenSum


numbers = [19, 10, 10, 11, 0]
print(odd_even_max_while(numbers))
print(odd_even_max_for(numbers))
print(odd_even_max_noloops(numbers))
