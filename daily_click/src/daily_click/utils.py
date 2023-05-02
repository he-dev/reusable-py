import click
from enum import Enum
from typing import TypeVar, Type


E = TypeVar("E", bound=Enum)


def parse_choice(factory: Type[E]):
    def _parse(ctx, param, value) -> None:
        values = list(map(lambda e: e.value, factory))
        param.type = click.Choice(values)
        param.expose_value = False
        if value:
            ctx.params[param.name] = factory(value)

    return _parse
