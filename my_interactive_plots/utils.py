import logging

def setup_logging():
    """
    Configures logging for the package.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    logger = logging.getLogger('my_interactive_plots')
    return logger

