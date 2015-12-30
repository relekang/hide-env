import os
import sys

import click

__version__ = '1.0.0'


@click.command()
@click.argument('variables', nargs=-1)
def hide_env(variables):
    text = sys.stdin.read()
    for variable_name in variables:
        variable_content = os.environ.get(variable_name)
        if variable_content:
            text = text.replace(variable_content, '[{0}]'.format(variable_name))
    sys.stdout.write(text)

if __name__ == '__main__':
    hide_env()
