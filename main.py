import logging
import argparse


def set_verbose(verbose, logfilepath=None):
    if verbose:
        if logfilepath is None:
            logging.basicConfig(level=logging.DEBUG, 
                                format='%(levelname)s: %(message)s')
        else:
            logging.basicConfig(filename=logfilepath, 
                                filemode='w', # overwrites at each run
                                level=logging.DEBUG, 
                                format='%(levelname)s: %(message)s')

def main():
    # set up a parser from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()

    # set the config for the logging based on command line flags
    set_verbose(verbose=args.verbose,
                logfilepath='log.txt')

    # program logic starts here
    print("run the program")
    a = 2
    if a == 2:
        logging.debug("This is a debug message. a = 2.")



if __name__ == "__main__":
    main()