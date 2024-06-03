from LoggerSetup import LoggerSetup
from sub1 import program_logic_two


def program_logic_one():
    # include this line here in every file that needs logging
    logger = LoggerSetup().get_logger()

    # logic starts from here
    logger.info("Program logic one started")
    a = 2
    if a == 2:
        logger.debug("This is a debug message from program logic one. a = 2.")
    else:
        logger.warning("Warning from program logic one: a is not 2")
    logger.error("this is an error message from program logic one.")
    logger.info("Program logic one ended")


if __name__ == "__main__":
    # Initial setup - only do once
    LoggerSetup(logfilepath=None)

    # Multiple usage cases
    program_logic_one()
    program_logic_two()
