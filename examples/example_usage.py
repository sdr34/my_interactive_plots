# examples/example_usage.py

from my_interactive_plots import create_plot

def main():
    """
    Example usage of the my_interactive_plots package.
    """
    data_path = 'data/iris.csv'  # Replace with your data path
    plot_types = ['scatter', 'line', 'histogram', 'box']
    
    for plot_type in plot_types:
        fig = create_plot(data_path, plot_type=plot_type)
        fig.show(title=f"{plot_type.capitalize()} Plot")

if __name__ == "__main__":
    main()
