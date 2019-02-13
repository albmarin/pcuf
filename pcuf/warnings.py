# -*- coding: utf-8 -*-
import warnings
from typing import Union

warnings.simplefilter("always", DeprecationWarning)


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
    warnings.warn(DeprecationWarning(message), stacklevel=2)
