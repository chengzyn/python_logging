import argparse
import logging


def set_logging(level, logfilepath=None):
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    if logfilepath:
        logging.basicConfig(filename=logfilepath, filemode='w', level=level, format=log_format)
    else:
        logging.basicConfig(level=level, format=log_format)


def main():
    # Set up a parser from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Enable debug level logging')
    parser.add_argument('--info', action='store_true', help='Enable info level logging')
    parser.add_argument('--warning', action='store_true', help='Enable warning level logging')
    parser.add_argument('--error', action='store_true', help='Enable error level logging')
    parser.add_argument('--critical', action='store_true', help='Enable critical level logging')
    args = parser.parse_args()

    # Determine the logging level based on the most critical flag given
    if args.debug:
        log_level = logging.DEBUG
    elif args.info:
        log_level = logging.INFO
    elif args.warning:
        log_level = logging.WARNING
    elif args.error:
        log_level = logging.ERROR
    elif args.critical:
        log_level = logging.CRITICAL
    else:
        log_level = logging.WARNING  # Default level if no flag is provided

    # Set the configuration for the logging based on command line flags
    set_logging(level=log_level, logfilepath=None)

    # Program logic starts here
    logging.info("Program started")
    a = 2
    if a == 2:
        logging.debug("This is a debug message. a = 2.")
    else:
        logging.warning("Warning: a is not 2")

    logging.error("This is just an error message for demonstration")

    logging.info("Program ended")


if __name__ == "__main__":
    main()
