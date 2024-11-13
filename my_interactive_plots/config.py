import json
import pathlib
from typing import Any

class Config:
    """
    Configuration settings for plots.
    """
    x_column: str = 'sepal_width'
    y_column: str = 'sepal_length'
    z_column: str = 'petal_length'       # For 3D plots
    latitude_column: str = 'latitude'     # For geographical maps
    longitude_column: str = 'longitude'   # For geographical maps
    hover_name: str = 'species'           # For geographical maps
    color_column: str = 'species'         # For color coding
    title: str = 'Sepal Width vs Sepal Length'
    theme: str = 'plotly_dark'            # Example theme
    marker_size: int = 10                 # Example customization

    def save_to_file(self, file_path: str):
        """
        Saves the current configuration to a JSON file.

        Args:
            file_path (str): Path to the JSON file.
        """
        config_dict = self.__dict__
        with open(file_path, 'w') as f:
            json.dump(config_dict, f, indent=4)

    def load_from_file(self, file_path: str):
        """
        Loads configuration settings from a JSON file.

        Args:
            file_path (str): Path to the JSON file.
        """
        with open(file_path, 'r') as f:
            config_dict = json.load(f)
        self.__dict__.update(config_dict)
