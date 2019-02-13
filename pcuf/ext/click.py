# -*- coding: utf-8 -*-
from typing import Iterable
import click


def add_commands(click_group: click.core.Group, commands: Iterable):
    for command in commands:
        if not isinstance(command, click.core.Command) and not isinstance(
            command, click.core.Group
        ):
            raise TypeError(
                f"commands must be of type click.core.Command or click.core.Group, got {type(command)}"
            )

        click_group.add_command(command)
