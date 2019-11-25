"""Command Line Interface (CLI) for this project."""



# The main entry point for tasks.
@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1.0')
def lcpy_cli():
    """Run the tasks application."""


if __name__ == '__main__':
    lcpy_cli()
