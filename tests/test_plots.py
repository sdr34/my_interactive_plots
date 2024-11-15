# tests/test_plots.py

import unittest
import pandas as pd
from my_interactive_plots.plots import create_plot
from my_interactive_plots.exceptions import PlotCreationError

class TestPlots(unittest.TestCase):
    def setUp(self):
        self.data_path = 'data/iris.csv'
        self.data = pd.read_csv(self.data_path)

    def test_create_scatter_plot(self):
        fig = create_plot(self.data, 'scatter')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))

    def test_create_line_plot(self):
        fig = create_plot(self.data, 'line')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))

    def test_create_histogram(self):
        fig = create_plot(self.data, 'histogram')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))

    def test_create_box_plot(self):
        fig = create_plot(self.data, 'box')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))

    def test_create_3d_scatter_plot(self):
        fig = create_plot(self.data, '3d_scatter')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))

    def test_create_geographical_map(self):
        # Assuming your data has 'latitude' and 'longitude' columns
        fig = create_plot(self.data, 'geo_map')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))

    def test_invalid_plot_type(self):
        with self.assertRaises(PlotCreationError):
            create_plot(self.data, 'invalid_type')

if __name__ == '__main__':
    unittest.main()
