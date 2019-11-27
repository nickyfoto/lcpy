"""Command Line Interface (CLI) for this project."""
import shutil
import inspect
from pprint import pprint
import os
import click

from .utils import gen_test, gen_params
import importlib


# The main entry point for cli.
@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1.0')
def lcpy_cli():
    """Run the tasks application."""

@lcpy_cli.command(help="check filename")
@click.argument('filename')
def cp(filename):
    """
    copy file and save it in tests folder
    """
    click.echo(filename)
    ud_fn = filename.replace('-', '_') #underline file name
    fl = ud_fn.split('.') #filename in list
    n = fl[0]
    base_dir = './tests/'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    module_name = f'{n}_{fl[1]}'
    # shutil.copy(filename, module_name+'.py')
    target_fn = f'{base_dir}{module_name}.py'
    # print(target_fn)
    shutil.copy(filename, target_fn)

    params = gen_params(module_name, target_fn)
    gen_test(n, module_name, params)

    








    # with open(f'test_{n}.py', 'w') as f:
        # f.write(s)

if __name__ == '__main__':
    lcpy_cli()
