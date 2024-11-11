import logging

def setup_logging():
    """
    Configures the logging for the package.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )


def helper_function():
    """
    A helper function for utility purposes.
    """
    pass  # Implement utility functionality here
