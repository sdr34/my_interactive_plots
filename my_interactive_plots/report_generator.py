import logging
import pandas as pd
from weasyprint import HTML
from .utils import setup_logging

# Configure logging
setup_logging()
logger = logging.getLogger(__name__)

def generate_report(data: pd.DataFrame, plot_types: list, report_file: str):
    """
    Generates an HTML report with the specified plots.

    Args:
        data (pd.DataFrame): The data to include in the report.
        plot_types (list): List of plot types to include.
        report_file (str): Path to save the report.
    """
    logger.info("Generating report")
    try:
        from .plots import create_plot  # Import here to allow mocking during tests
        
        html_content = "<html><head><title>Data Report</title></head><body>"
        html_content += "<h1>Data Report</h1>"

        for plot_type in plot_types:
            fig = create_plot(data, plot_type)
            fig_html = fig.to_html(full_html=False)
            html_content += f"<h2>{plot_type.capitalize()} Plot</h2>"
            html_content += fig_html

        html_content += "</body></html>"

        HTML(string=html_content).write_pdf(report_file)
        logger.info(f"Report saved to {report_file}")
    except Exception as e:
        logger.error(f"Failed to generate report: {e}")
        raise

def generate_profile_report(data: pd.DataFrame, profile_file: str):
    """
    Generates a data profile report.

    Args:
        data (pd.DataFrame): The data to profile.
        profile_file (str): Path to save the profile report.
    """
    logger.info("Generating profile report")
    try:
        import pandas_profiling

        profile = pandas_profiling.ProfileReport(data, title="Data Profile Report")
        profile.to_file(profile_file)
        logger.info(f"Data profile report saved to {profile_file}")
    except Exception as e:
        logger.error(f"Failed to generate profile report: {e}")
        raise



