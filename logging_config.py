import logging

def setup_logging():
    """
    Sets up logging configuration.

    Configures the logging settings to output log messages to the console with
    a specific format. The logging level is set to DEBUG to capture all levels
    of log messages. The log messages include the timestamp, logger name, log
    level, and message content.

    Handlers:
        logging.StreamHandler: Outputs log messages to the console.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )
