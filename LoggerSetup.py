import argparse
import logging
import threading


class LoggerSetup:
    """
    Uses a singleton design pattern that ensures logging is configured only once.
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LoggerSetup, cls).__new__(cls)
        return cls._instance

    def __init__(self, logfilepath=None):
        if not hasattr(self, 'initialized'):  # Ensure __init__ runs only once
            self.logfilepath = logfilepath
            self.log_level = logging.WARNING  # Default log level
            self.configure_logging()
            self.initialized = True

    def configure_logging(self):
        args = self.parse_arguments()
        self.determine_log_level(args)
        self.set_logging()

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('--debug', action='store_true', help='Enable debug level logging')
        parser.add_argument('--info', action='store_true', help='Enable info level logging')
        parser.add_argument('--warning', action='store_true', help='Enable warning level logging')
        parser.add_argument('--error', action='store_true', help='Enable error level logging')
        parser.add_argument('--critical', action='store_true', help='Enable critical level logging')
        return parser.parse_args()

    def determine_log_level(self, args):
        if args.debug:
            self.log_level = logging.DEBUG
        elif args.info:
            self.log_level = logging.INFO
        elif args.warning:
            self.log_level = logging.WARNING
        elif args.error:
            self.log_level = logging.ERROR
        elif args.critical:
            self.log_level = logging.CRITICAL
        else:
            self.log_level = logging.WARNING  # Default level if no flag is provided

    def set_logging(self):
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        if self.logfilepath:
            logging.basicConfig(filename=self.logfilepath, filemode='w', level=self.log_level, format=log_format)
        else:
            logging.basicConfig(level=self.log_level, format=log_format)

    def get_logger(self):
        return logging.getLogger()
