from my_interactive_plots import create_plot

def main():
    """
    Example usage of the my_interactive_plots package.
    """
    data_path = 'data/iris.csv'  # Replace with your data path
    fig = create_plot(data_path)
    fig.show()

if __name__ == "__main__":
    main()
