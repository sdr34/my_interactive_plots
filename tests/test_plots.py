import unittest
from my_interactive_plots.plots import create_plot

class TestPlots(unittest.TestCase):
    def setUp(self):
        self.data_path = 'data/iris.csv'
    
    def test_create_scatter_plot(self):
        fig = create_plot(self.data_path, 'scatter')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))
    
    def test_create_line_plot(self):
        fig = create_plot(self.data_path, 'line')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))
    
    def test_create_histogram(self):
        fig = create_plot(self.data_path, 'histogram')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))
    
    def test_create_box_plot(self):
        fig = create_plot(self.data_path, 'box')
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))
    
    def test_invalid_plot_type(self):
        with self.assertRaises(ValueError):
            create_plot(self.data_path, 'invalid_type')

if __name__ == '__main__':
    unittest.main()

