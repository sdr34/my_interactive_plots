from typing import Any, cast
import plotly.io as pio
import pandas as pd  # Убедитесь, что pandas импортирован
from .plots import create_plot

def generate_report(data: pd.DataFrame, plot_types: list, output_file: str):
    """
    Генерирует HTML-отчет с несколькими графиками.

    Args:
        data (pd.DataFrame): DataFrame с данными.
        plot_types (list): Список типов графиков для включения в отчет.
        output_file (str): Путь для сохранения HTML-отчета.
    """
    with open(output_file, 'w') as f:
        f.write("<html><head><title>Report</title></head><body>")
        f.write("<h1>Data Report</h1>")
        for plot_type in plot_types:
            fig = create_plot(data, plot_type)
            # Используйте правильные типы для параметра include_plotlyjs
            plot_html = pio.to_html(fig, include_plotlyjs=cast(Any, 'cdn'), full_html=False)
            f.write(f"<h2>{plot_type.capitalize()} Plot</h2>")
            f.write(plot_html)
        f.write("</body></html>")

