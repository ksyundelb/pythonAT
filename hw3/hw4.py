"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so on.
You may assume that every list contains at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    if not args:
        return [[]]
    else:
        result = []
        for item in args[0]:
            for subcombination in combinations(*args[1:]):
                result.append([item] + subcombination)
        return result
