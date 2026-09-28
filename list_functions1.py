# Starter file for list manipulation assignments

"""
List Functions 1

Functions for practicing list manipulation.
"""


def zip2lists(list1, list2):
    result = []

    for i in range(len(list1)):
        result.append([list1[i], list2[i]])

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


def interleave_lists(list1, list2):
    result = []

    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])

    return result


def remove_even_indices(lst):
    result = []

    for i in range(len(lst)):
        if i % 2 != 0:
            result.append(lst[i])

    return result


def repeat_elements(lst, n):
    result = []

    for element in lst:
        for i in range(n):
            result.append(element)

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