# -*- coding: utf-8 -*-
import logging
from typing import Callable

logger = logging.getLogger(__name__)


def retry(func: Callable, retries: int = 3, *args, **kwargs):
    """Attempts to call a given function that may throw an exception x number of times,
     or until it runs without error."""
    err = None
    for idx in range(retries):
        try:
            logger.debug(f"Executing {func.__name__} function...{idx + 1}")
            return func(*args, **kwargs)
        except Exception as e:
            logger.debug(
                f"{func.__name__} function threw {e.__class__.__name__}. Retrying..."
            )
            err = e

    logger.debug(f"{func.__name__}  execution failed! Raising exception...")
    raise err
