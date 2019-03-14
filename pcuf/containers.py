import copy
from itertools import zip_longest


def lookahead(iterable):
    """Pass through all values from the given iterable, augmented by the
    information if there are more values to come after the current one
    (True), or if it is the last value (False).
    """
    # Get an iterator and pull the first value.
    it = iter(iterable)
    last = next(it)

    # Run the iterator to exhaustion (starting from the second value).
    for val in it:
        # Report the *previous* value (more to come).
        yield last, True
        last = val

    # Report the last value.
    yield last, False


def haskey(element, keys, default=None, return_remaining=False):
    """
    Check if keys (nested) exists in `element` (dict).
    """
    if element is None or keys is None:
        return default

    if not isinstance(element, dict):
        raise TypeError(f"haskey() expects dict as element, got {type(element)}")

    if not isinstance(keys, list):
        raise TypeError(
            f"haskey() expects list of object type str as keys, got {type(keys)}"
        )

    _element = element
    _keys = copy.deepcopy(keys)
    for key in _keys[:]:
        try:
            _element = _element[key]
            _keys.remove(key)
        except KeyError:
            if return_remaining:
                return default, (_element, _keys)
            return default

    if return_remaining:
        return _element, (_element, _keys)
    return _element


def assign_key(element, keys, value=None):
    if element is None or keys is None:
        return None

    if not isinstance(element, dict):
        raise TypeError(f"assign_key() expects dict as element, got {type(element)}")

    if not isinstance(keys, list):
        raise TypeError(
            f"assign_key() expects list of object type str as keys, got {type(keys)}"
        )

    _element = element
    for key, has_more in lookahead(keys):
        if has_more:
            if haskey(_element, [key]):
                _element = _element[key]
                continue
            _element[key] = {}
            _element = _element[key]

        else:
            _element[key] = value

    return element


def grouper(n, iterable, sentinel=None):
    return [
        [entry for entry in item if entry is not sentinel]
        for item in zip_longest(*[iter(iterable)] * n, fillvalue=sentinel)
    ]
