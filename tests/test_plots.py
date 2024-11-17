# tests/test_plots.py

import unittest
import pandas as pd
from unittest.mock import patch
from my_interactive_plots.plots import (
    create_plot,
    create_scatter_plot,
    create_line_plot,
    create_histogram,
    create_box_plot,
    create_3d_scatter_plot,
    create_geographical_map,
    create_combined_plot,
    create_animated_scatter_plot,
    PlotCreationError
)

class TestPlots(unittest.TestCase):
    def setUp(self):
        # Данные для тестов без географической информации
        self.data = pd.DataFrame({
            'sepal_length': [5.1, 4.9, 4.7],
            'sepal_width': [3.5, 3.0, 3.2],
            'petal_length': [1.4, 1.4, 1.3],
            'petal_width': [0.2, 0.2, 0.2],
            'species': ['Setosa', 'Setosa', 'Setosa']
        })
        
        # Данные для geo_map
        self.geo_data = pd.DataFrame({
            'latitude': [34.05, 36.16, 40.71],
            'longitude': [-118.24, -115.15, -74.00],
            'species': ['Setosa', 'Versicolor', 'Virginica']
        })
        
        # Данные для animated_scatter
        self.animated_data = pd.DataFrame({
            'sepal_length': [5.1, 4.9, 4.7],
            'sepal_width': [3.5, 3.0, 3.2],
            'petal_length': [1.4, 1.4, 1.3],
            'petal_width': [0.2, 0.2, 0.2],
            'species': ['Setosa', 'Setosa', 'Setosa'],
            'animation_frame': ['Setosa', 'Setosa', 'Setosa']
        })

    @patch('my_interactive_plots.plots.px.scatter')
    def test_create_scatter_plot_success(self, mock_scatter):
        mock_scatter.return_value = 'FigureObject'
        fig = create_scatter_plot(self.data)
        self.assertEqual(fig, 'FigureObject')
        mock_scatter.assert_called_once()

    @patch('my_interactive_plots.plots.px.scatter')
    def test_create_scatter_plot_failure(self, mock_scatter):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_scatter_plot(invalid_data)

    @patch('my_interactive_plots.plots.px.line')
    def test_create_line_plot_success(self, mock_line):
        mock_line.return_value = 'LineFigureObject'
        fig = create_line_plot(self.data)
        self.assertEqual(fig, 'LineFigureObject')
        mock_line.assert_called_once()

    @patch('my_interactive_plots.plots.px.line')
    def test_create_line_plot_failure(self, mock_line):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_line_plot(invalid_data)

    @patch('my_interactive_plots.plots.px.histogram')
    def test_create_histogram_success(self, mock_histogram):
        mock_histogram.return_value = 'HistogramFigureObject'
        fig = create_histogram(self.data)
        self.assertEqual(fig, 'HistogramFigureObject')
        mock_histogram.assert_called_once()

    @patch('my_interactive_plots.plots.px.histogram')
    def test_create_histogram_failure(self, mock_histogram):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_histogram(invalid_data)

    @patch('my_interactive_plots.plots.px.box')
    def test_create_box_plot_success(self, mock_box):
        mock_box.return_value = 'BoxFigureObject'
        fig = create_box_plot(self.data)
        self.assertEqual(fig, 'BoxFigureObject')
        mock_box.assert_called_once()

    @patch('my_interactive_plots.plots.px.box')
    def test_create_box_plot_failure(self, mock_box):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_box_plot(invalid_data)

    @patch('my_interactive_plots.plots.px.scatter_3d')
    def test_create_3d_scatter_plot_success(self, mock_scatter_3d):
        mock_scatter_3d.return_value = '3DScatterFigureObject'
        fig = create_3d_scatter_plot(self.data)
        self.assertEqual(fig, '3DScatterFigureObject')
        mock_scatter_3d.assert_called_once()

    @patch('my_interactive_plots.plots.px.scatter_3d')
    def test_create_3d_scatter_plot_failure(self, mock_scatter_3d):
        # Удаляем обязательный столбец 'petal_length' (z_column)
        invalid_data = self.data.drop(columns=['petal_length'])
        with self.assertRaises(PlotCreationError):
            create_3d_scatter_plot(invalid_data)

    @patch('my_interactive_plots.plots.px.scatter_geo')
    def test_create_geographical_map_success(self, mock_scatter_geo):
        mock_scatter_geo.return_value = 'GeoMapFigureObject'
        fig = create_geographical_map(self.geo_data)
        self.assertEqual(fig, 'GeoMapFigureObject')
        mock_scatter_geo.assert_called_once()

    def test_create_geographical_map_failure_missing_latitude(self):
        # Удаляем столбец 'latitude'
        invalid_data = self.geo_data.drop(columns=['latitude'])
        with self.assertRaises(PlotCreationError):
            create_geographical_map(invalid_data)

    def test_create_geographical_map_failure_missing_longitude(self):
        # Удаляем столбец 'longitude'
        invalid_data = self.geo_data.drop(columns=['longitude'])
        with self.assertRaises(PlotCreationError):
            create_geographical_map(invalid_data)

    @patch('my_interactive_plots.plots.go.Figure')
    def test_create_combined_plot_success(self, mock_figure):
        mock_figure.return_value = 'CombinedFigureObject'
        fig = create_combined_plot(self.data)
        self.assertEqual(fig, 'CombinedFigureObject')
        mock_figure.assert_called_once()

    def test_create_combined_plot_failure(self):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_combined_plot(invalid_data)

    @patch('my_interactive_plots.plots.px.scatter')
    def test_create_animated_scatter_plot_success(self, mock_scatter):
        mock_scatter.return_value = 'AnimatedScatterFigureObject'
        fig = create_animated_scatter_plot(self.animated_data, 'animation_frame')
        self.assertEqual(fig, 'AnimatedScatterFigureObject')
        mock_scatter.assert_called_once()

    @patch('my_interactive_plots.plots.px.scatter')
    def test_create_animated_scatter_plot_failure_missing_animation_frame(self, mock_scatter):
        # Убедитесь, что столбца 'animation_frame' нет
        with self.assertRaises(PlotCreationError):
            create_animated_scatter_plot(self.data, 'animation_frame')

    @patch('my_interactive_plots.plots.px.scatter')
    @patch('my_interactive_plots.plots.px.line')
    @patch('my_interactive_plots.plots.px.histogram')
    @patch('my_interactive_plots.plots.px.box')
    @patch('my_interactive_plots.plots.px.scatter_3d')
    @patch('my_interactive_plots.plots.px.scatter_geo')
    def test_create_plot_valid_types(self, mock_scatter_geo, mock_scatter_3d, mock_box, mock_histogram, mock_line, mock_scatter):
        # Mock all plot functions to return 'FigureObject'
        mock_scatter.return_value = 'ScatterFigureObject'
        mock_line.return_value = 'LineFigureObject'
        mock_histogram.return_value = 'HistogramFigureObject'
        mock_box.return_value = 'BoxFigureObject'
        mock_scatter_3d.return_value = '3DScatterFigureObject'
        mock_scatter_geo.return_value = 'GeoMapFigureObject'

        plot_types = [
            'scatter',
            'line',
            'histogram',
            'box',
            '3d_scatter',
            'geo_map',
            'combined',
            'animated_scatter'
        ]

        for plot_type in plot_types:
            if plot_type == 'geo_map':
                fig = create_plot(self.geo_data, plot_type)
                self.assertEqual(fig, 'GeoMapFigureObject')
            elif plot_type == 'animated_scatter':
                fig = create_plot(self.animated_data, plot_type, animation_frame='animation_frame')
                self.assertEqual(fig, 'AnimatedScatterFigureObject')
            else:
                fig = create_plot(self.data, plot_type)
                if plot_type == 'scatter':
                    self.assertEqual(fig, 'ScatterFigureObject')
                elif plot_type == 'line':
                    self.assertEqual(fig, 'LineFigureObject')
                elif plot_type == 'histogram':
                    self.assertEqual(fig, 'HistogramFigureObject')
                elif plot_type == 'box':
                    self.assertEqual(fig, 'BoxFigureObject')
                elif plot_type == '3d_scatter':
                    self.assertEqual(fig, '3DScatterFigureObject')
                elif plot_type == 'combined':
                    self.assertEqual(fig, 'CombinedFigureObject')

    def test_create_plot_invalid_type(self):
        with self.assertRaises(PlotCreationError):
            create_plot(self.data, 'invalid_type')

if __name__ == '__main__':
    unittest.main()
