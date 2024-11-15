# my_interactive_plots/plots.py

import logging
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from .data_loader import load_data
from .config import Config
from .exceptions import PlotCreationError
from .utils import setup_logging

# Configure logging
setup_logging()
logger = logging.getLogger(__name__)

def create_scatter_plot(data: pd.DataFrame) -> go.Figure:
    """
    Creates an interactive scatter plot using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating scatter plot")
    config = Config()
    try:
        fig = px.scatter(
            data, 
            x=config.x_column, 
            y=config.y_column, 
            color=config.color_column,
            title=config.title,
            template=config.theme
        )
        return fig
    except Exception as e:
        logger.error(f"Failed to create scatter plot: {e}")
        raise PlotCreationError("Failed to create scatter plot") from e

def create_line_plot(data: pd.DataFrame) -> go.Figure:
    """
    Creates an interactive line plot using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating line plot")
    config = Config()
    try:
        fig = px.line(
            data,
            x=config.x_column,
            y=config.y_column,
            color=config.color_column,
            title=config.title,
            template=config.theme
        )
        return fig
    except Exception as e:
        logger.error(f"Failed to create line plot: {e}")
        raise PlotCreationError("Failed to create line plot") from e

def create_histogram(data: pd.DataFrame) -> go.Figure:
    """
    Creates an interactive histogram using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating histogram")
    config = Config()
    try:
        fig = px.histogram(
            data,
            x=config.x_column,
            color=config.color_column,
            title=config.title,
            template=config.theme
        )
        return fig
    except Exception as e:
        logger.error(f"Failed to create histogram: {e}")
        raise PlotCreationError("Failed to create histogram") from e

def create_box_plot(data: pd.DataFrame) -> go.Figure:
    """
    Creates an interactive box plot using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating box plot")
    config = Config()
    try:
        fig = px.box(
            data,
            x=config.x_column,
            y=config.y_column,
            color=config.color_column,
            title=config.title,
            template=config.theme
        )
        return fig
    except Exception as e:
        logger.error(f"Failed to create box plot: {e}")
        raise PlotCreationError("Failed to create box plot") from e

def create_3d_scatter_plot(data: pd.DataFrame) -> go.Figure:
    """
    Creates an interactive 3D scatter plot using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating 3D scatter plot")
    config = Config()
    try:
        fig = px.scatter_3d(
            data, 
            x=config.x_column, 
            y=config.y_column, 
            z=config.z_column, 
            color=config.color_column,
            title=config.title,
            template=config.theme
        )
        return fig
    except Exception as e:
        logger.error(f"Failed to create 3D scatter plot: {e}")
        raise PlotCreationError("Failed to create 3D scatter plot") from e

def create_geographical_map(data: pd.DataFrame) -> go.Figure:
    """
    Creates an interactive geographical map using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating geographical map")
    config = Config()
    try:
        fig = px.scatter_geo(
            data,
            lat=config.latitude_column,
            lon=config.longitude_column,
            hover_name=config.hover_name,
            color=config.color_column,
            title=config.title,
            template=config.theme
        )
        return fig
    except Exception as e:
        logger.error(f"Failed to create geographical map: {e}")
        raise PlotCreationError("Failed to create geographical map") from e

def create_combined_plot(data: pd.DataFrame) -> go.Figure:
    """
    Creates a combined plot with multiple chart types using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating combined plot")
    config = Config()
    try:
        fig = go.Figure()

        # Add scatter plot
        fig.add_trace(go.Scatter(
            x=data[config.x_column],
            y=data[config.y_column],
            mode='markers',
            name='Scatter'
        ))

        # Add line plot (rolling mean)
        fig.add_trace(go.Scatter(
            x=data[config.x_column],
            y=data[config.y_column].rolling(window=5).mean(),
            mode='lines',
            name='Rolling Mean'
        ))

        fig.update_layout(
            title=config.title,
            template=config.theme
        )

        return fig
    except Exception as e:
        logger.error(f"Failed to create combined plot: {e}")
        raise PlotCreationError("Failed to create combined plot") from e

def create_animated_scatter_plot(data: pd.DataFrame, animation_frame: str) -> go.Figure:
    """
    Creates an animated scatter plot using Plotly.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        animation_frame (str): Column name to use for animation frames.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info("Creating animated scatter plot")
    config = Config()
    try:
        fig = px.scatter(
            data,
            x=config.x_column,
            y=config.y_column,
            color=config.color_column,
            animation_frame=animation_frame,
            title=config.title,
            template=config.theme
        )
        return fig
    except Exception as e:
        logger.error(f"Failed to create animated scatter plot: {e}")
        raise PlotCreationError("Failed to create animated scatter plot") from e

def create_plot(data: pd.DataFrame, plot_type: str, **kwargs) -> go.Figure:
    """
    Creates an interactive plot based on the specified plot type.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        plot_type (str): Type of plot to create. Options: 'scatter', 'line', 'histogram', 'box', '3d_scatter', 'geo_map', 'combined', 'animated_scatter'.
        **kwargs: Additional keyword arguments for specific plot types.

    Returns:
        go.Figure: Plotly figure object.
    """
    logger.info(f"Creating plot of type: {plot_type}")
    try:
        if plot_type == 'scatter':
            return create_scatter_plot(data)
        elif plot_type == 'line':
            return create_line_plot(data)
        elif plot_type == 'histogram':
            return create_histogram(data)
        elif plot_type == 'box':
            return create_box_plot(data)
        elif plot_type == '3d_scatter':
            return create_3d_scatter_plot(data)
        elif plot_type == 'geo_map':
            return create_geographical_map(data)
        elif plot_type == 'combined':
            return create_combined_plot(data)
        elif plot_type == 'animated_scatter':
            animation_frame = kwargs.get('animation_frame')
            if not animation_frame:
                raise ValueError("Missing required argument: 'animation_frame'")
            return create_animated_scatter_plot(data, animation_frame)
        else:
            raise ValueError(f"Unsupported plot type: {plot_type}")
    except Exception as e:
        logger.error(f"Failed to create plot of type {plot_type}: {e}")
        raise PlotCreationError(f"Failed to create plot of type {plot_type}") from e
