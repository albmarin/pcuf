# -*- coding: utf-8 -*-
import warnings
from typing import Union


class SimpleDeprecationWarning(DeprecationWarning):
    pass


warnings.simplefilter("always", SimpleDeprecationWarning)


def deprecate(
    message: str,
    version: Union[int, float, str] = None,
    link_uid: str = None,
    link_file: str = None,
):
    """Displays a deprecation warning"""
    if version:
        message += "\nIt will be compatible before version {}.".format(version)
    if link_uid and link_file:
        message += "\nRead more <https://git.io/{}#file-{}-md>".format(
            link_uid, link_file
        )
    warnings.warn(SimpleDeprecationWarning(message), stacklevel=2)
