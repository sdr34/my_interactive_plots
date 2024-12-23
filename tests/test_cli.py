# tests/test_cli.py

import unittest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from build.lib.my_interactive_plots.exceptions import PlotCreationError
from my_interactive_plots.cli import cli
import pandas as pd
import os
import shutil
import tempfile

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        # Создаём временную директорию для изолированной файловой системы
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        
        # Пути к тестовым файлам внутри временной директории
        self.valid_data_path = os.path.join(self.temp_dir.name, 'iris.csv')
        self.geo_data_path = os.path.join(self.temp_dir.name, 'geo_data.csv')
        self.invalid_data_path = os.path.join(self.temp_dir.name, 'nonexistent.csv')
        
        # Создаём sample iris.csv
        iris_data = pd.DataFrame({
            'sepal_length': [5.1, 4.9, 4.7],
            'sepal_width': [3.5, 3.0, 3.2],
            'petal_length': [1.4, 1.4, 1.3],
            'petal_width': [0.2, 0.2, 0.2],
            'species': ['Setosa', 'Setosa', 'Setosa']
        })
        iris_data.to_csv(self.valid_data_path, index=False)
        
        # Создаём sample geo_data.csv
        geo_data = pd.DataFrame({
            'latitude': [34.05, 36.16, 40.71],
            'longitude': [-118.24, -115.15, -74.00],
            'species': ['Setosa', 'Versicolor', 'Virginica']
        })
        geo_data.to_csv(self.geo_data_path, index=False)

    @patch('my_interactive_plots.plots.create_plot')
    def test_cli_scatter_plot_success(self, mock_create_plot):
        mock_fig = MagicMock()
        mock_create_plot.return_value = mock_fig
        result = self.runner.invoke(cli, [self.valid_data_path, '--plot-type', 'scatter'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Scatter plot created successfully.', result.output)
        mock_create_plot.assert_called_once_with(pd.read_csv(self.valid_data_path), 'scatter')

    @patch('my_interactive_plots.plots.create_plot')
    def test_cli_line_plot_success(self, mock_create_plot):
        mock_fig = MagicMock()
        mock_create_plot.return_value = mock_fig
        result = self.runner.invoke(cli, [self.valid_data_path, '--plot-type', 'line'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Line plot created successfully.', result.output)
        mock_create_plot.assert_called_once_with(pd.read_csv(self.valid_data_path), 'line')

    @patch('my_interactive_plots.plots.create_plot')
    def test_cli_geo_map_success(self, mock_create_plot):
        mock_fig = MagicMock()
        mock_create_plot.return_value = mock_fig
        result = self.runner.invoke(cli, [self.geo_data_path, '--plot-type', 'geo_map'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Geo_map plot created successfully.', result.output)
        mock_create_plot.assert_called_once_with(pd.read_csv(self.geo_data_path), 'geo_map')

    @patch('my_interactive_plots.plots.create_plot')
    def test_cli_geo_map_failure_missing_columns(self, mock_create_plot):
        # Используем iris.csv, который не содержит 'latitude' и 'longitude'
        mock_create_plot.side_effect = PlotCreationError("Failed to create geographical map")
        result = self.runner.invoke(cli, [self.valid_data_path, '--plot-type', 'geo_map'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn('Error: Failed to create plot of type geo_map', result.output)
        mock_create_plot.assert_called_once_with(pd.read_csv(self.valid_data_path), 'geo_map')

    def test_cli_invalid_plot_type(self):
        result = self.runner.invoke(cli, [self.valid_data_path, '--plot-type', 'invalid_type'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Invalid value for '--plot-type': 'invalid_type' is not one of 'scatter', 'line', 'histogram', 'box', '3d_scatter', 'geo_map', 'combined', 'animated_scatter'.", result.output)

    def test_cli_missing_data_source(self):
        result = self.runner.invoke(cli, ['--plot-type', 'scatter'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing argument 'DATA_SOURCE'", result.output)

    @patch('my_interactive_plots.report_generator.generate_report')
    def test_cli_generate_report_success(self, mock_generate_report):
        mock_generate_report.return_value = None  # Assume success
        with self.runner.isolated_filesystem():
            # Копируем iris.csv в изолированную файловую систему
            shutil.copy(self.valid_data_path, 'iris.csv')
            result = self.runner.invoke(cli, [
                'iris.csv',
                '--plot-type', 'scatter',
                '--save-report',
                '--output', 'report.html'
            ])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Report saved to report.html', result.output)
            mock_generate_report.assert_called_once_with(pd.read_csv('iris.csv'), ['scatter'], 'report.html')

    @patch('my_interactive_plots.report_generator.generate_report')
    def test_cli_generate_report_failure_invalid_output_format(self, mock_generate_report):
        mock_generate_report.side_effect = PlotCreationError("Unsupported export format.")
        with self.runner.isolated_filesystem():
            # Копируем iris.csv в изолированную файловую систему
            shutil.copy(self.valid_data_path, 'iris.csv')
            result = self.runner.invoke(cli, [
                'iris.csv',
                '--plot-type', 'scatter',
                '--save-report',
                '--output', 'report.txt'  # Unsupported format
            ])
            self.assertNotEqual(result.exit_code, 0)
            self.assertIn('Error: Unsupported export format.', result.output)
            mock_generate_report.assert_called_once_with(pd.read_csv('iris.csv'), ['scatter'], 'report.txt')

    @patch('my_interactive_plots.report_generator.generate_profile_report')
    def test_cli_generate_profile_report_success(self, mock_generate_profile_report):
        mock_generate_profile_report.return_value = None  # Assume success
        with self.runner.isolated_filesystem():
            # Копируем iris.csv в изолированную файловую систему
            shutil.copy(self.valid_data_path, 'iris.csv')
            result = self.runner.invoke(cli, [
                'iris.csv',
                '--plot-type', 'scatter',
                '--generate-profile',
                '--output', 'profile_report.html'
            ])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Data profile report saved to profile_report.html', result.output)
            mock_generate_profile_report.assert_called_once_with(pd.read_csv('iris.csv'), 'profile_report.html')

    @patch('my_interactive_plots.report_generator.generate_profile_report')
    def test_cli_generate_profile_report_failure(self, mock_generate_profile_report):
        mock_generate_profile_report.side_effect = FileNotFoundError("Data source not found.")
        result = self.runner.invoke(cli, [
            self.invalid_data_path,
            '--plot-type', 'scatter',
            '--generate-profile'
        ])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn('Error: Data source not found', result.output)
        mock_generate_profile_report.assert_called_once_with(pd.read_csv(self.invalid_data_path), 'profile_report.html')

if __name__ == '__main__':
    unittest.main()
