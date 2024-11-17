import pandas as pd
import sqlalchemy
from pandas.errors import DataError
from .exceptions import PlotCreationError

def load_data(file_path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Data source not found: {file_path}")
    except DataError:
        raise PlotCreationError(f"Error parsing the data file: {file_path}")
    except Exception as e:
        raise PlotCreationError(f"An error occurred while loading data: {e}") from e

def load_data_from_db(connection_string: str, query: str) -> pd.DataFrame:
    """
    Loads data from a database using SQL query.

    Args:
        connection_string (str): Database connection string.
        query (str): SQL query to execute.

    Returns:
        pd.DataFrame: Loaded data.
    """
    engine = sqlalchemy.create_engine(connection_string)
    return pd.read_sql_query(query, engine)
