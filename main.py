from LoggerSetup import logger_setup
import logging


def main():
    # set up the logger
    logger_setup()

    # Program logic starts here
    logging.info("Program started")
    logging.debug("This is a debug message")
    logging.warning("This is just a warning message for demonstration")
    logging.error("This is just an error message for demonstration")
    logging.critical("This is just a critical message for demonstration")
    logging.info("Program ended")

    sub()


def sub():
    logging.info("Test info")


if __name__ == "__main__":
    main()
