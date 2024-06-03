from LoggerSetup import LoggerSetup


def program_logic_two():
    # include this line here in every file that needs logging
    logger = LoggerSetup().get_logger()

    # logic starts from here
    logger.info("Program logic two started")
    b = 3
    if b == 3:
        logger.debug("This is a debug message from program logic two. b = 3.")
    else:
        logger.warning("Warning from program logic two: b is not 3")
    logger.critical("This is a critical message from program logic two. b = 3.")
    logger.info("Program logic two ended")
