#!/usr/bin/env python
import sys

import click
from loguru import logger

from {{ cookiecutter.project_python }}.{{ cookiecutter.project_python }} import (
    {{ cookiecutter.project_python }},
)


@click.command()
@click.option(
    "--url", required=True, help="URL, e.g. https://example.com"
)
def cli(
    url,
):
    """
    HTTP Call CLI
    """

    {{ cookiecutter.project_python }}(
        url,
    )


if __name__ == "__main__":
    logger.remove(0)
    logger.add(sys.stdout, format='time={time} level={level} msg="{message}"')
    cli()
