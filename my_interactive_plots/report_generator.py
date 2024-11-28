# my_interactive_plots/report_generator.py

import logging
import pandas as pd
from weasyprint import HTML
from .utils import setup_logging
from .exceptions import PlotCreationError
from pandas.errors import DataError  # Правильный импорт

# Configure logging
setup_logging()
logger = logging.getLogger(__name__)

def generate_report(data: pd.DataFrame, plot_types: list, report_file: str):
    """
    Generates an HTML report with the specified plots.
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
    except ImportError as e:
        logger.error(f"ImportError: {e}")
        raise PlotCreationError("Failed to import necessary modules for report generation") from e
    except Exception as e:
        logger.error(f"Failed to generate report: {e}")
        raise PlotCreationError("Failed to generate report") from e

def generate_profile_report(data: pd.DataFrame, profile_file: str):
    """
    Generates a data profile report.
    """
    logger.info("Generating profile report")
    try:
        import pandas_profiling

        profile = pandas_profiling.ProfileReport(data, title="Data Profile Report")
        profile.to_file(profile_file)
        logger.info(f"Data profile report saved to {profile_file}")
    except ImportError as e:
        logger.error(f"ImportError: {e}")
        raise PlotCreationError("Failed to import pandas_profiling for profile report generation") from e
    except Exception as e:
        logger.error(f"Failed to generate profile report: {e}")
        raise PlotCreationError("Failed to generate profile report") from e


