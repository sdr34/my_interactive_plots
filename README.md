# My Interactive Plots

![Downloads](https://static.pepy.tech/personalized-badge/my-interactive-plots?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads)

[![PyPI version](https://badge.fury.io/py/my-interactive-plots.svg)](https://badge.fury.io/py/my-interactive-plots)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://github.com/sdr34/my_interactive_plots/actions/workflows/python-app.yml/badge.svg)](https://github.com/sdr34/my_interactive_plots/actions)

A Python package for creating interactive plots using Plotly. Supports various plot types and includes a Command-Line Interface (CLI) for ease of use.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
  - [Python API](#python-api)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
- [Supported Plot Types](#supported-plot-types)
- [Configuration](#configuration)
- [Logging](#logging)
- [Testing](#testing)
- [Continuous Integration](#continuous-integration)
- [Contributing](#contributing)
- [License](#license)

## Installation

Ensure you have **Python 3.6+** installed.

### Using `pip`

You can install the package directly from PyPI:

```bash
pip install my-interactive-plots
```
## From Source

Clone the repository and install in editable mode:

```bash

git clone https://github.com/sdr34/my_interactive_plots.git
cd my_interactive_plots
pip install -e .
```

## Features

+ Interactive Plots: Create scatter, line, histogram, and box plots using Plotly.
+ Command-Line Interface (CLI): Generate plots directly from the terminal.
+ Configurable Settings: Customize plot parameters via configuration files.
+ Logging: Track operations and debug effectively.
+ Comprehensive Testing: Ensure reliability with unit tests.
+ Continuous Integration: Automated testing with GitHub Actions.

## Usage

## Python API

Use the package within your Python scripts to generate interactive plots.

```python
from my_interactive_plots import create_plot

def main():
    data_path = 'data/iris.csv'  # Path to your CSV data file
    plot_type = 'scatter'        # Choose from 'scatter', 'line', 'histogram', 'box'
    
    fig = create_plot(data_path, plot_type=plot_type)
    fig.show()

if __name__ == "__main__":
    main()
```
## Command-Line Interface (CLI)

After installation, you can use the `myplot` command in your terminal to create plots.

Examples

Create a scatter plot:

```bash

myplot data/iris.csv --plot-type scatter
```
Create a line plot:

```bash
myplot data/iris.csv --plot-type line
```
Create a histogram:

```bash
myplot data/iris.csv --plot-type histogram
```
Create a box plot:

```bash

myplot data/iris.csv --plot-type box
```
## Options

+ `DATA_SOURCE`: Path to the CSV data file.
+ `--plot-type`: Type of plot to create (`scatter`, `line`, `histogram`, `box`). Default is `scatter`.

## Supported Plot Types

+ ***Scatter Plot***: Visualize relationships between two variables.
+ ***Line Plot***: Show trends over time or continuous data.
+ ***Histogram***: Display the distribution of a single variable.
+ ***Box Plot***: Summarize distributions and identify outliers.

## Configuration

Plot settings are defined in `config.py`. You can customize the plot by modifying the configuration.

```python
# my_interactive_plots/config.py

class Config:
    """
    Configuration settings for plots.
    """
    x_column = 'sepal_width'
    y_column = 'sepal_length'
    title = 'Sepal Width vs Sepal Length'
```
## Customizing Plot Settings

To change the columns used for the axes or the plot title, edit the `Config` class in `config.py`:

```python
class Config:
    x_column = 'petal_width'    # Changed from 'sepal_width'
    y_column = 'petal_length'   # Changed from 'sepal_length'
    title = 'Petal Width vs Petal Length'  # Updated title
```
After making changes, rerun your script or CLI command to see the updated plot.


## Logging

Logging is set up to track the package's operations. Logs are output to the console, providing insights into the package's behavior and aiding in debugging.

## Customizing Logging

The logging configuration can be adjusted in `utils.py`:

```python
# my_interactive_plots/utils.py

import logging

def setup_logging():
    """
    Configures the logging for the package.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
```
## Testing

The project includes unit tests to ensure functionality.

## Running Tests

To run the tests, use:

```bash
python -m unittest discover tests
```
Ensure that you have the necessary test data (`data/iris.csv`) in place before running tests.

## Test Coverage
The tests cover:

+ Creation of different plot types.
+ Handling of invalid plot types.
+ CLI functionality.

## Continuous Integration

The project uses GitHub Actions for Continuous Integration (CI). Tests are automatically run on each push and pull request to the `main` branch.

## GitHub Actions Workflow

The workflow is defined in `.github/workflows/python-app.yml`. It sets up Python, installs dependencies, and runs tests.

```yaml
# .github/workflows/python-app.yml

name: Python package

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .
        pip install pytest click

    - name: Run tests
      run: |
        pytest
```
## Viewing CI Results

Check the "Actions" tab in your GitHub repository to view the status of CI runs.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the Repository: Click the "Fork" button on the repository page.

2. Clone Your Fork:

```bash
git clone https://github.com/sdr34/my_interactive_plots.git
cd my_interactive_plots
```
3. Create a New Branch:

```bash
git checkout -b feature/your-feature-name
```
4. Make Your Changes: Implement your feature or bugfix.
5. Commit Your Changes:

```bash
git commit -m "Add feature: your feature description"
```
6. Push to Your Fork:

```bash
git push origin feature/your-feature-name
```
7. Open a Pull Request: Navigate to the original repository and open a pull request from your fork.

## Coding Standards

+ Follow PEP 8 guidelines.
+ Write clear and concise commit messages.
+ Ensure all tests pass before submitting a pull request.

## License

his project is licensed under the MIT License. See the LICENSE file for details.

## Additional Notes


+ ***Data Directory***: Ensure that the data/iris.csv file exists in the data directory. You can add your own datasets as needed.
+ ***Virtual Environment***: It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment before installing the package.

## Creating a Virtual Environment

```bash
python -m venv venv
```
Activate the virtual environment:

+ On Windows:

```bash
venv\Scripts\activate
```
+ On macOS/Linux:

```bash
source venv/bin/activate
```
## Installing Dependencies

```bash
pip install -e .
```
## Deactivating the Virtual Environment

After you're done, deactivate the virtual environment:
```bash
deactivate
```
## Troubleshooting

+ ***FileNotFoundError***: Ensure that the `data/iris.csv` file exists and the path is correct.
+ ***Module Not Found Errors***: Make sure the package is installed correctly in your environment.
+ ***Plot Not Displaying***: Check if you have a default web browser set up, as Plotly opens plots in the browser.

For further assistance, feel free to open an issue in the repository.