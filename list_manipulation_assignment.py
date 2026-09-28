def sum_list(lst):
    total = 0

    for value in lst:
        total += value

    return total


def contains_element(lst, element):
    for value in lst:
        if value == element:
            return True

    return False


def index_of_element(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i

    return len(lst) + 1


def minimum(lst):
    smallest = lst[0]

    for value in lst:
        if value < smallest:
            smallest = value

    return smallest


def index_of_minimum(lst):
    smallest_index = 0

    for i in range(1, len(lst)):
        if lst[i] < lst[smallest_index]:
            smallest_index = i

    return smallest_index


def remove_even_indices(lst):
    result = []

    for i in range(len(lst)):
        if i % 2 != 0:
            result.append(lst[i])

    return result


def square_list(lst):
    result = []

    for value in lst:
        result.append(value * value)

    return result


def remove_negatives(lst):
    result = []

    for value in lst:
        if value >= 0:
            result.append(value)

    return result


def cumulative_sum(lst):
    result = []
    total = 0

    for value in lst:
        total += value
        result.append(total)

    return result


def middle(lst):
    if len(lst) == 0:
        return None

    middle_index = len(lst) // 2

    if len(lst) % 2 == 1:
        return lst[middle_index]

    return [lst[middle_index - 1], lst[middle_index]]


def remove_duplicates(lst):
    result = []

    for value in lst:
        if value not in result:
            result.append(value)

    return result


def isIncreasing(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False

    return True


def evenIndicesIncreasing(lst):
    for i in range(2, len(lst), 2):
        if lst[i] != lst[i - 2] + 1:
            return False

    return True


def positionOfLastFromEnd(lst, element):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == element:
            return len(lst) - 1 - i

    return -(len(lst) + 1)


def add(lst, amount):
    result = []

    for value in lst:
        result.append(value + amount)

    return result


def addList(list1, list2):
    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result


def reverse(lst):
    result = []

    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])

    return result


def reverse_pairs(lst):
    result = []
    i = 0

    while i < len(lst):
        if i + 1 < len(lst):
            result.append(lst[i + 1])
            result.append(lst[i])
        else:
            result.append(lst[i])

        i += 2

    return result


def repeat_elements(lst, n):
    result = []

    for value in lst:
        for i in range(n):
            result.append(value)

    return result


def expand_encoded_string(encoded):
    result = ""
    i = 0

    while i < len(encoded):
        letter = encoded[i]
        i += 1

        number = ""

        while i < len(encoded) and encoded[i].isdigit():
            number += encoded[i]
            i += 1

        if number != "":
            result += letter * int(number)

    return result