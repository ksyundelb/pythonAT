from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:

    most_common = max(set(inp), key=inp.count)
    least_common = min(set(inp), key=inp.count)
    return most_common, least_common