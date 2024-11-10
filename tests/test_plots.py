import unittest
from my_interactive_plots.plots import create_plot

class TestPlots(unittest.TestCase):
    def test_create_plot(self):
        """
        Test if create_plot returns a Plotly figure.
        """
        fig = create_plot('data/iris.csv')  # Ensure this path is valid for tests
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'show'))

if __name__ == '__main__':
    unittest.main()


