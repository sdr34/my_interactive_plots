from my_interactive_plots import create_plot
import pandas as pd
from pathlib import Path

def main():
    current_dir = Path(__file__).parent
    data_path = current_dir.parent / 'data' / 'iris.csv'
    
    plot_type = 'scatter'
    
    if not data_path.exists():
        print(f"Data file not found at path: {data_path}")
        return
    
    data = pd.read_csv(data_path)

    if plot_type == 'animated_scatter':
        fig = create_plot(data, plot_type=plot_type, animation_frame='species')
    else:
        fig = create_plot(data, plot_type=plot_type)
    
    fig.show()

if __name__ == "__main__":
    main()

