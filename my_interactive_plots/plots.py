import logging
import plotly.express as px
from .data_loader import load_data
from .config import Config
from .utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def create_scatter_plot(data_source: str):
    """
    Create an interactive scatter plot using Plotly.
    
    Args:
        data_source (str): Path to the data file.
    
    Returns:
        fig: Plotly figure object.
    """
    logger.info(f"Creating scatter plot from {data_source}")
    data = load_data(data_source)
    config = Config()
    fig = px.scatter(data, x=config.x_column, y=config.y_column, title=config.title)
    return fig

def create_line_plot(data_source: str):
    """
    Create an interactive line plot using Plotly.
    
    Args:
        data_source (str): Path to the data file.
    
    Returns:
        fig: Plotly figure object.
    """
    logger.info(f"Creating line plot from {data_source}")
    data = load_data(data_source)
    config = Config()
    fig = px.line(data, x=config.x_column, y=config.y_column, title=config.title)
    return fig

def create_histogram(data_source: str):
    """
    Create an interactive histogram using Plotly.
    
    Args:
        data_source (str): Path to the data file.
    
    Returns:
        fig: Plotly figure object.
    """
    logger.info(f"Creating histogram from {data_source}")
    data = load_data(data_source)
    config = Config()
    fig = px.histogram(data, x=config.x_column, title=config.title)
    return fig

def create_box_plot(data_source: str):
    """
    Create an interactive box plot using Plotly.
    
    Args:
        data_source (str): Path to the data file.
    
    Returns:
        fig: Plotly figure object.
    """
    logger.info(f"Creating box plot from {data_source}")
    data = load_data(data_source)
    config = Config()
    fig = px.box(data, y=config.y_column, title=config.title)
    return fig

def create_plot(data_source: str, plot_type: str = 'scatter'):
    """
    Create an interactive plot based on the specified type.
    
    Args:
        data_source (str): Path to the data file.
        plot_type (str): Type of plot to create ('scatter', 'line', 'histogram', 'box').
    
    Returns:
        fig: Plotly figure object.
    """
    logger.info(f"Creating plot from {data_source}")
    if plot_type == 'scatter':
        return create_scatter_plot(data_source)
    elif plot_type == 'line':
        return create_line_plot(data_source)
    elif plot_type == 'histogram':
        return create_histogram(data_source)
    elif plot_type == 'box':
        return create_box_plot(data_source)
    else:
        raise ValueError(f"Unsupported plot type: {plot_type}. Choose from 'scatter', 'line', 'histogram', 'box'.")
