import click
import logging

log_console = logging.StreamHandler()
log_console.setLevel(logging.INFO)
format_console = logging.Formatter("%(levelname)s [%(module)s : %(message)s]")
log_console.setFormatter(format_console)
logging.basicConfig(level=logging.NOTSET, handlers=[log_console])

logger = logging.getLogger(__name__)

CONFIG_FILE = "~/wlj-config.yaml"

config_option = click.option(
    "--config", "-c", default=CONFIG_FILE, help="Specify the config file"
)


@click.group(chain=True)
def cli():
    # Empty on purpose, just for command grouping
    pass


@cli.command()
@click.option("--log", default="~/.worklog", help="Specify worklog to read")
@click.option("--server", help="The server for uploading the worklog")
@click.argument("time", default="today")
@config_option
def up(log, server, time):
    """
    Uploads then worklog
    """
    click.echo(f"Server: {server}")


@cli.command()
def info():
    """
    Prints some general information
    """
    click.echo("Thanks for using wlj!")
