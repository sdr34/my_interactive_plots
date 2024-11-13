import click
import logging
from .plots import create_plot
from .utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@click.command()
@click.argument('data_source', type=click.Path(exists=True))
@click.option(
    '--plot-type', 
    default='scatter', 
    type=click.Choice(['scatter', 'line', 'histogram', 'box', '3d_scatter', 'geo_map']), 
    help='Type of plot to create.'
)
@click.option(
    '--output', 
    type=click.Path(), 
    help='Path to save the plot (e.g., plot.html, plot.png).'
)
@click.option(
    '--export-format', 
    type=click.Choice(['html', 'png', 'pdf', 'svg']), 
    default='html', 
    help='Format to export the plot.'
)
@click.option(
    '--filter-column', 
    type=str, 
    help='Column name to filter data.'
)
@click.option(
    '--filter-value', 
    type=str, 
    help='Value to filter the column by.'
)
def cli(data_source, plot_type, output, export_format, filter_column, filter_value):
    """
    Command-Line Interface for creating interactive plots.

    DATA_SOURCE: Path to the CSV or Excel data file.
    """
    try:
        import pandas as pd
        from .data_loader import load_data

        data = load_data(data_source)
        if filter_column and filter_value:
            data = data[data[filter_column] == filter_value]
            logger.info(f"Filtered data where {filter_column} == {filter_value}")

        fig = create_plot(data, plot_type)

        if output:
            if export_format == 'html':
                fig.write_html(output)
            elif export_format in ['png', 'pdf', 'svg']:
                fig.write_image(output)
            else:
                raise ValueError("Unsupported export format. Please use HTML or image formats like PNG, PDF, SVG.")
            click.echo(f"Plot saved to {output}")
        else:
            fig.show()
            click.echo(f"{plot_type.capitalize()} plot created successfully.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        click.echo(f"Error: {e}")
