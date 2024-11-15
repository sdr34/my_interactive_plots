import pandas as pd
import sqlalchemy

def load_data(data_source: str) -> pd.DataFrame:
    """
    Loads data from a CSV or Excel file into a DataFrame.

    Args:
        data_source (str): Path to the data file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    if data_source.endswith('.csv'):
        return pd.read_csv(data_source)
    elif data_source.endswith(('.xls', '.xlsx')):
        return pd.read_excel(data_source)
    else:
        raise ValueError("Unsupported file format. Please use CSV or Excel files.")

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
