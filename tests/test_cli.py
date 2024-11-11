import unittest
from click.testing import CliRunner
from my_interactive_plots.cli import cli

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.data_path = 'data/iris.csv'
    
    def test_cli_scatter_plot(self):
        result = self.runner.invoke(cli, [self.data_path, '--plot-type', 'scatter'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Scatter plot created successfully.', result.output)
    
    def test_cli_invalid_plot_type(self):
        result = self.runner.invoke(cli, [self.data_path, '--plot-type', 'invalid'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn('Error: Invalid value for "--plot-type"', result.output)

if __name__ == '__main__':
    unittest.main()
