from LoggerSetup import LoggerSetup


def program_logic_one():
    # include this line here in every file that needs logging
    logger = LoggerSetup().get_logger()

    # logic starts from here
    logger.info("Program logic one started")
    logger.debug("This is a debug message from program logic one")
    logger.warning("Warning from program logic one")
    logger.critical("This is a critical message from program logic one")
    logger.info("Program logic one ended")
