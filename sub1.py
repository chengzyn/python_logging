from LoggerSetup import LoggerSetup


def program_logic_one():
    """
    one of the two separate functions that use the logger. It calls "LoggerSetup().get_logger()" to get the
    configured logger instance.
    """
    # include this line here in every file that needs logging
    logger = LoggerSetup().get_logger()

    # logic starts from here
    logger.info("Program logic one started")
    logger.debug("This is a debug message from program logic one")
    logger.warning("Warning from program logic one")
    logger.critical("This is a critical message from program logic one")
    logger.info("Program logic one ended\n")
