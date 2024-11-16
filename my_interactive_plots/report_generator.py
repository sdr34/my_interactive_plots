import plotly.io as pio
import pandas as pd
from .plots import create_plot

def generate_report(data: pd.DataFrame, plot_types: list, output_file: str):
    """
    Generates an HTML report with multiple plots.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        plot_types (list): List of plot types to include in the report.
        output_file (str): Path to save the HTML report.
    """
    with open(output_file, 'w') as f:
        f.write("<html><head><title>Report</title></head><body>")
        f.write("<h1>Data Report</h1>")
        for plot_type in plot_types:
            fig = create_plot(data, plot_type)
            # Use correct types for the include_plotlyjs parameter
            plot_html = pio.to_html(fig, include_plotlyjs='cdn', full_html=False) # type: ignore
            f.write(f"<h2>{plot_type.capitalize()} Plot</h2>")
            f.write(plot_html)
        f.write("</body></html>")

def generate_profile_report(data: pd.DataFrame, output_file: str):
    """
    Generates a descriptive data report using pandas_profiling.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        output_file (str): Path to save the HTML profile report.
    """
    from pandas_profiling import ProfileReport
    
    profile = ProfileReport(data, title="Data Profiling Report", explorative=True)
    profile.to_file(output_file)


