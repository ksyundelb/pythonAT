def flatten(items):
    for x in items:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x

def merge_elems(*elems):
    for elem in flatten(elems):
        yield elem


def map_like(fun, *elems):
    for elem in elems:
        try:
            yield fun(elem)
        except TypeError:
            yield f"{elem}: {type(elem).__name__} object is not subscriptable"