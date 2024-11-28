# tests/test_plots.py

import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
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
        mock_fig = MagicMock()
        mock_scatter.return_value = mock_fig
        fig = create_scatter_plot(self.data)
        self.assertEqual(fig, mock_fig)
        mock_scatter.assert_called_once_with(
            self.data, 
            x='sepal_width', 
            y='sepal_length', 
            color='species',
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

    @patch('my_interactive_plots.plots.px.scatter')
    def test_create_scatter_plot_failure(self, mock_scatter):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_scatter_plot(invalid_data)
        mock_scatter.assert_not_called()

    @patch('my_interactive_plots.plots.px.line')
    def test_create_line_plot_success(self, mock_line):
        mock_fig = MagicMock()
        mock_line.return_value = mock_fig
        fig = create_line_plot(self.data)
        self.assertEqual(fig, mock_fig)
        mock_line.assert_called_once_with(
            self.data,
            x='sepal_width',
            y='sepal_length',
            color='species',
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

    @patch('my_interactive_plots.plots.px.line')
    def test_create_line_plot_failure(self, mock_line):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_line_plot(invalid_data)
        mock_line.assert_not_called()

    @patch('my_interactive_plots.plots.px.histogram')
    def test_create_histogram_success(self, mock_histogram):
        mock_fig = MagicMock()
        mock_histogram.return_value = mock_fig
        fig = create_histogram(self.data)
        self.assertEqual(fig, mock_fig)
        mock_histogram.assert_called_once_with(
            self.data,
            x='sepal_width',
            color='species',
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

    @patch('my_interactive_plots.plots.px.histogram')
    def test_create_histogram_failure(self, mock_histogram):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_histogram(invalid_data)
        mock_histogram.assert_not_called()

    @patch('my_interactive_plots.plots.px.box')
    def test_create_box_plot_success(self, mock_box):
        mock_fig = MagicMock()
        mock_box.return_value = mock_fig
        fig = create_box_plot(self.data)
        self.assertEqual(fig, mock_fig)
        mock_box.assert_called_once_with(
            self.data,
            x='sepal_width',
            y='sepal_length',
            color='species',
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

    @patch('my_interactive_plots.plots.px.box')
    def test_create_box_plot_failure(self, mock_box):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_box_plot(invalid_data)
        mock_box.assert_not_called()

    @patch('my_interactive_plots.plots.px.scatter_3d')
    def test_create_3d_scatter_plot_success(self, mock_scatter_3d):
        mock_fig = MagicMock()
        mock_scatter_3d.return_value = mock_fig
        fig = create_3d_scatter_plot(self.data)
        self.assertEqual(fig, mock_fig)
        mock_scatter_3d.assert_called_once_with(
            self.data, 
            x='sepal_width', 
            y='sepal_length', 
            z='petal_length', 
            color='species',
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

    @patch('my_interactive_plots.plots.px.scatter_3d')
    def test_create_3d_scatter_plot_failure(self, mock_scatter_3d):
        # Удаляем обязательный столбец 'petal_length' (z_column)
        invalid_data = self.data.drop(columns=['petal_length'])
        with self.assertRaises(PlotCreationError):
            create_3d_scatter_plot(invalid_data)
        mock_scatter_3d.assert_not_called()

    @patch('my_interactive_plots.plots.px.scatter_geo')
    def test_create_geographical_map_success(self, mock_scatter_geo):
        mock_fig = MagicMock()
        mock_scatter_geo.return_value = mock_fig
        fig = create_geographical_map(self.geo_data)
        self.assertEqual(fig, mock_fig)
        mock_scatter_geo.assert_called_once_with(
            self.geo_data,
            lat='latitude',
            lon='longitude',
            hover_name='species',
            color='species',
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

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
    def test_create_combined_plot_success(self, mock_figure_class):
        mock_fig = MagicMock()
        mock_figure_class.return_value = mock_fig
        fig = create_combined_plot(self.data)
        self.assertEqual(fig, mock_fig)
        mock_figure_class.assert_called_once_with()
        # Проверяем, что add_trace был вызван дважды
        self.assertEqual(mock_fig.add_trace.call_count, 2)
        # Проверяем, что update_layout был вызван один раз
        mock_fig.update_layout.assert_called_once_with(
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

    def test_create_combined_plot_failure_missing_x_column(self):
        # Удаляем обязательный столбец 'sepal_width' (x_column)
        invalid_data = self.data.drop(columns=['sepal_width'])
        with self.assertRaises(PlotCreationError):
            create_combined_plot(invalid_data)

    @patch('my_interactive_plots.plots.px.scatter')
    def test_create_animated_scatter_plot_success(self, mock_scatter):
        mock_fig = MagicMock()
        mock_scatter.return_value = mock_fig
        fig = create_animated_scatter_plot(self.animated_data, 'animation_frame')
        self.assertEqual(fig, mock_fig)
        mock_scatter.assert_called_once_with(
            self.animated_data,
            x='sepal_width',
            y='sepal_length',
            color='species',
            animation_frame='animation_frame',
            title='Sepal Width vs Sepal Length',
            template='plotly_dark'
        )

    @patch('my_interactive_plots.plots.px.scatter')
    def test_create_animated_scatter_plot_failure_missing_animation_frame(self, mock_scatter):
        # Убедитесь, что столбца 'animation_frame' нет
        with self.assertRaises(PlotCreationError):
            create_animated_scatter_plot(self.data, 'animation_frame')
        mock_scatter.assert_not_called()

    @patch('my_interactive_plots.plots.create_geographical_map')
    @patch('my_interactive_plots.plots.create_3d_scatter_plot')
    @patch('my_interactive_plots.plots.create_box_plot')
    @patch('my_interactive_plots.plots.create_histogram')
    @patch('my_interactive_plots.plots.create_line_plot')
    @patch('my_interactive_plots.plots.create_scatter_plot')
    @patch('my_interactive_plots.plots.create_combined_plot')
    @patch('my_interactive_plots.plots.create_animated_scatter_plot')
    def test_create_plot_valid_types(self, mock_animated_scatter, mock_combined_plot, mock_scatter_plot, mock_line_plot, mock_histogram, mock_box_plot, mock_3d_scatter_plot, mock_geographical_map):
        # Устанавливаем моки
        mock_scatter_plot.return_value = MagicMock()
        mock_line_plot.return_value = MagicMock()
        mock_histogram.return_value = MagicMock()
        mock_box_plot.return_value = MagicMock()
        mock_3d_scatter_plot.return_value = MagicMock()
        mock_geographical_map.return_value = MagicMock()
        mock_combined_plot.return_value = MagicMock()
        mock_animated_scatter.return_value = MagicMock()

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
                self.assertIsNotNone(fig)
                mock_geographical_map.assert_called_once_with(self.geo_data)
            elif plot_type == 'animated_scatter':
                fig = create_plot(self.animated_data, plot_type, animation_frame='animation_frame')
                self.assertIsNotNone(fig)
                mock_animated_scatter.assert_called_once_with(self.animated_data, 'animation_frame')
            else:
                fig = create_plot(self.data, plot_type)
                self.assertIsNotNone(fig)
                if plot_type == 'scatter':
                    mock_scatter_plot.assert_called_once_with(self.data)
                elif plot_type == 'line':
                    mock_line_plot.assert_called_once_with(self.data)
                elif plot_type == 'histogram':
                    mock_histogram.assert_called_once_with(self.data)
                elif plot_type == 'box':
                    mock_box_plot.assert_called_once_with(self.data)
                elif plot_type == '3d_scatter':
                    mock_3d_scatter_plot.assert_called_once_with(self.data)
                elif plot_type == 'combined':
                    mock_combined_plot.assert_called_once_with(self.data)

    @patch('my_interactive_plots.plots.create_plot')
    def test_create_plot_invalid_type(self, mock_create_plot):
        with self.assertRaises(PlotCreationError):
            create_plot(self.data, 'invalid_type')
        mock_create_plot.assert_not_called()

if __name__ == '__main__':
    unittest.main()
