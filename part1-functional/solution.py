"""
solution.py

This script defines a function `remove_duplicates` that removes duplicate elements
from a list while preserving the original order of first occurrences.

Example test cases are also included to demonstrate the functions behavior.

"""

def remove_duplicates(arr):
    """
    Remove duplicates from a list while preserving the original order
    of first occurrences.

    args:
        arr (list): Input list containing elements of hashable type.

    returns:
        list: A new list containing only the first occurrence of each element.

    """
    seen = set() # elements that have been encountered
    # keep an element only if it has not been encountered before otherwise, skip it
    return list(filter(lambda x: not (x in seen or seen.add(x)), arr))

# test cases 
print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1]))              # [1]
print(remove_duplicates([]))                     # []
