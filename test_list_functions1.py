# Test file using assertions for all 6 functions
from list_manipulation_assignment import (
    expand_encoded_string,
    remove_even_indices,
    repeat_elements,
    reverse,
    reverse_pairs,
    square_list,
    remove_negatives,
    cumulative_sum,
    middle,
    remove_duplicates,
    sum_list,
    contains_element,
    index_of_element,
    minimum,
    index_of_minimum,
    isIncreasing,
    evenIndicesIncreasing,
    positionOfLastFromEnd,
    add,
    addList
)

# 1. Test sum_list
assert sum_list([1, 2, 3]) == 6
assert sum_list([]) == 0
assert sum_list([10]) == 10

# 2 Test contains_element
assert contains_element([1, 2, 3], 2) == True
assert contains_element([1, 2, 3], 5) == False
assert contains_element([], 0) == False

# 3 Test index_of_element
assert index_of_element(["a", "b", "c"], "b") == 1
assert index_of_element(["a", "b", "c"], "z") == 4
assert index_of_element([], "x") == 1

# 4 Test minimum
assert minimum([3, 1, 4]) == 1
assert minimum([5]) == 5

# 5 Test index_of_minimum
assert index_of_minimum([3, 1, 4]) == 1
assert index_of_minimum([5]) == 0


# 6 Test remove_even_indices
assert remove_even_indices([10, 20, 30, 40, 50]) == [20, 40]
assert remove_even_indices(["x", "y", "z"]) == ["y"]
assert remove_even_indices([]) == []

# 7. Test square_list
assert square_list([1, 2, 3]) == [1, 4, 9]
assert square_list([-1, 0, 2]) == [1, 0, 4]
assert square_list([]) == []

# 8. Test remove_negatives
assert remove_negatives([-1, 2, -3, 4]) == [2, 4]
assert remove_negatives([0, 5, 7]) == [0, 5, 7]
assert remove_negatives([]) == []

# 9. Test cumulative_sum
assert cumulative_sum([1, 2, 3]) == [1, 3, 6]
assert cumulative_sum([5]) == [5]
assert cumulative_sum([]) == []

# 10. Test middle
assert middle([1, 2, 3]) == 2
assert middle([1, 2, 3, 4]) == [2, 3]
assert middle([]) == None
assert middle([7]) == 7

# 11. Test remove_duplicates
assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
assert remove_duplicates([]) == []



# 12 --- Tests for isIncreasing ---
assert isIncreasing([1, 2, 3]) == True
assert isIncreasing([1, 1, 2]) == False
assert isIncreasing([5]) == True
assert isIncreasing([]) == True

# 13 --- Tests for evenIndicesIncreasing ---
assert evenIndicesIncreasing([1, 3, 2, 4]) == True   # evens = [1, 2]
assert evenIndicesIncreasing([2, 5, 4, 7]) == False  # evens = [2, 4] (not strictly increasing with single step)
assert evenIndicesIncreasing([10]) == True
assert evenIndicesIncreasing([]) == True

# 14 --- Tests for positionOfLastFromEnd ---
# Empty list
assert positionOfLastFromEnd([], 5) == -1
# No 5 in list of length 1
assert positionOfLastFromEnd([41], 5) == -2
# No 5 in list of length 2
assert positionOfLastFromEnd([31, 41], 5) == -3
# No 5 in list of length 3
assert positionOfLastFromEnd([21, 31, 41], 5) == -4
# No 5 in list of length 4
assert positionOfLastFromEnd([11, 21, 31, 41], 5) == -5
# 5 present
assert positionOfLastFromEnd([5, 11, 21, 31, 41], 5) == 4
assert positionOfLastFromEnd([5, 5, 11, 21, 31, 41], 5) == 4
assert positionOfLastFromEnd([1, 5, 5, 11, 21, 31, 41], 5) == 4
assert positionOfLastFromEnd([5], 5) == 0
assert positionOfLastFromEnd([5, 31, 41], 5) == 2
assert positionOfLastFromEnd([21, 5, 31, 41], 5) == 2
assert positionOfLastFromEnd([5, 21, 5, 31, 41], 5) == 2

# 15 --- Tests for add ---
assert add([1, 5, 5, 11, 21, 31, 41], 3) == [4, 8, 8, 14, 24, 34, 44]
assert add([], 10) == []

# 16 --- Tests for addList ---
assert addList([1, 4, 5], [-2, 2, 8]) == [-1, 6, 13]
assert addList([], []) == []
assert addList([10], [5]) == [15]



# 17 --- Tests for reverse ---

# Empty list
assert reverse([]) == []

# Single element
assert reverse([1]) == [1]

# Two elements
assert reverse([1, 2]) == [2, 1]

# Multiple elements
assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
assert reverse(["a", "b", "c"]) == ["c", "b", "a"]

# Palindrome list (reversing gives same list)
assert reverse([1, 2, 3, 2, 1]) == [1, 2, 3, 2, 1]



# 18. Test reverse_pairs
assert reverse_pairs([1, 2, 3, 4]) == [2, 1, 4, 3]
assert reverse_pairs([1, 2, 3]) == [2, 1, 3]
assert reverse_pairs([]) == []
assert reverse_pairs([5]) == [5]

# 19. Test repeat_elements
assert repeat_elements(["a", "b"], 3) == ["a", "a", "a", "b", "b", "b"]
assert repeat_elements([], 5) == []
assert repeat_elements(["x"], 0) == []

# 20. Test expand_encoded_string
assert expand_encoded_string("A3b2") == "AAAbb"
assert expand_encoded_string("C1o2l1d1") == "Coold"

print("All tests passed!")
