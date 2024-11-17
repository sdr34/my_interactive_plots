import click
import pandas as pd
from .plots import create_plot, PlotCreationError
from .data_loader import load_data
from .config import Config
from .report_generator import generate_report, generate_profile_report

@click.command()
@click.argument('data_source')
@click.option('--plot-type', default='scatter', type=click.Choice(
    ['scatter', 'line', 'histogram', 'box', '3d_scatter', 'geo_map', 'combined', 'animated_scatter']),
    help='Type of plot: scatter, line, histogram, box, 3d_scatter, geo_map, combined, animated_scatter')
@click.option('--output', default=None, help='Path to save the plot or report')
@click.option('--export-format', type=click.Choice(['html', 'png', 'pdf', 'svg']), default='html', help='Format to export the plot')
@click.option('--filter-column', default=None, help='Name of the column to filter data')
@click.option('--filter-value', default=None, help='Value to filter data')
@click.option('--save-report', is_flag=True, help='Save report as an HTML file')
@click.option('--theme', default='plotly', type=click.Choice(
    ['plotly', 'plotly_white', 'plotly_dark', 'ggplot2', 'seaborn', 'simple_white']),
    help='Theme for the plots')
@click.option('--generate-profile', is_flag=True, help='Generate a descriptive data report')
def cli(data_source, plot_type, output, export_format, filter_column, filter_value, save_report, theme, generate_profile):
    """
    Command-line interface for creating interactive plots and reports.

    DATA_SOURCE: Path to the data file (CSV, Excel, JSON).
    """
    try:
        # Load data
        data = load_data(data_source)
        config = Config()
        config.theme = theme
        if filter_column and filter_value:
            if filter_column not in data.columns:
                raise ValueError(f"Filter column '{filter_column}' does not exist in the data.")
            data = data[data[filter_column] == filter_value]
        
        # Create plot
        if plot_type == 'animated_scatter':
            animation_frame = 'animation_frame'  # Ensure this column exists in data
            if animation_frame not in data.columns:
                raise ValueError(f"Animation frame column '{animation_frame}' does not exist in the data.")
            fig = create_plot(data, plot_type, animation_frame=animation_frame)
        else:
            fig = create_plot(data, plot_type)
        
        # Generate profile report if needed
        if generate_profile:
            profile_file = output if output else 'profile_report.html'
            generate_profile_report(data, profile_file)
            click.echo(f"Data profile report saved to {profile_file}")
        
        # Save report or plot
        if save_report:
            report_file = output if output else 'report.html'
            generate_report(data, [plot_type], report_file)
            click.echo(f"Report saved to {report_file}")
        else:
            if output:
                if export_format == 'html':
                    fig.write_html(output)
                elif export_format in ['png', 'pdf', 'svg']:
                    fig.write_image(output)
                else:
                    raise ValueError("Unsupported export format.")
                click.echo(f"Plot saved to {output}")
            else:
                fig.show()
                click.echo(f"{plot_type.capitalize()} plot created successfully.")
    except PlotCreationError as e:
        click.echo(f"Error: Failed to create plot of type {plot_type}")
    except ValueError as e:
        click.echo(f"Error: {e}")
    except FileNotFoundError as e:
        click.echo(f"Error: Data source not found - {e.filename}")
    except Exception as e:
        click.echo(f"Error: {e}")
