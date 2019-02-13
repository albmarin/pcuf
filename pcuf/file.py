# -*- coding: utf-8 -*-
import hashlib
import logging
from pathlib import Path

from click import confirm

logger = logging.getLogger(__name__)


def sha1(file: Path) -> str:
    """Returns SHA1 hash of file"""
    return hashlib.sha1(file.read_bytes()).hexdigest()


def rename(file: Path, new_name: str):
    """Ranames the given file with the given new name"""
    logger.debug(f"Renaming file: {file.name} to {new_name}")

    while True:
        try:
            file.rename(f"{file.parent / new_name}")
            break
        except PermissionError:
            logger.error(
                f"A permission error has occurred for file: `{file}`. "
                "It is likely that the file you are trying to rename "
                "is currently opened by another user."
            )

            try_again = confirm(
                "File could not be renamed. Would you like to try again?", default=True
            )

            if not try_again:
                break
