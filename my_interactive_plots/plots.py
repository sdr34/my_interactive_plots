import plotly.express as px
from .data_loader import load_data
from .config import Config

def create_plot(data_source: str):
    """
    Create an interactive plot using Plotly.

    Args:
        data_source (str): Path to the data file.

    Returns:
        fig: Plotly figure object.
    """
    data = load_data(data_source)
    config = Config()
    fig = px.scatter(data, x=config.x_column, y=config.y_column, title=config.title)
    return fig
