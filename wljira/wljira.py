import click
import logging

log_console = logging.StreamHandler()
log_console.setLevel(logging.INFO)
format_console = logging.Formatter("%(levelname)s [%(module)s : %(message)s]")
log_console.setFormatter(format_console)
logging.basicConfig(level=logging.NOTSET, handlers=[log_console])

logger = logging.getLogger(__name__)


@click.group(chain=True)
def cli():
    # Empty on purpose, just for command grouping
    pass


@cli.command()
def info():
    """
    Prints some general information
    """
    click.echo("Thanks for using wlj!")
