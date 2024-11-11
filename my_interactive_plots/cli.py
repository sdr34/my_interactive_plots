import click
import logging
from .plots import create_plot
from .utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@click.command()
@click.argument('data_source', type=click.Path(exists=True))
@click.option('--plot-type', default='scatter', type=click.Choice(['scatter', 'line', 'histogram', 'box']), help='Type of plot to create.')
def cli(data_source, plot_type):
    """
    Command-line interface for creating interactive plots.
    
    DATA_SOURCE: Path to the CSV data file.
    """
    try:
        logger.info(f"Generating {plot_type} plot for {data_source}")
        fig = create_plot(data_source, plot_type)
        fig.show()
        click.echo(f"{plot_type.capitalize()} plot created successfully.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        click.echo(f"Error: {e}")
