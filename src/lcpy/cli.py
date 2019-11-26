"""Command Line Interface (CLI) for this project."""


import click
# The main entry point for tasks.
@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1.0')
def lcpy_cli():
    """Run the tasks application."""

@lcpy_cli.command(help="check filename")
@click.argument('filename')
def lcpy_cp(filename):
	click.echo(filename)
	
if __name__ == '__main__':
    lcpy_cli()
