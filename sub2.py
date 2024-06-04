from LoggerSetup import LoggerSetup


def program_logic_two():
    """
    one of the two separate functions that use the logger. It calls "LoggerSetup().get_logger()" to get the
    configured logger instance.
    """
    # include this line here in every file that needs logging
    logger = LoggerSetup().get_logger()

    # logic starts from here
    logger.info("Program logic two started")
    logger.debug("This is a debug message from program logic two")
    logger.error("This is a error message from program logic two")
    logger.info("Program logic two ended\n")
