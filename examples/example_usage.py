from my_interactive_plots import create_plot
import pandas as pd

def main():
    data_path = 'data/iris.csv'  # Path to your CSV or Excel data file
    plot_type = 'scatter'        # Choose from 'scatter', 'line', 'histogram', 'box', '3d_scatter', 'geo_map'
    
    # Load data
    data = pd.read_csv(data_path)
    
    # Create plot
    fig = create_plot(data, plot_type=plot_type)
    
    # Show plot
    fig.show()

if __name__ == "__main__":
    main()
