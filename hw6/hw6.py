def flatten(items):
    for x in items:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x

def merge_elems(*elems):
    for elem in elems:
        if isinstance(elem, str) and len(elem) > 1:
            elem = list(elem)
        yield from flatten(elem)


def map_like(fun, *elems):
    for elem in elems:
        try:
            yield fun(elem)
        except Exception as e:
            yield f"{elem}: {type(e).__name__} - {str(e)}"