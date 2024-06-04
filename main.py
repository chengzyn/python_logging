from LoggerSetup import LoggerSetup
from sub1 import program_logic_one
from sub2 import program_logic_two

if __name__ == "__main__":
    # Instantiates the LoggerSetup class, thus configuring the logging
    LoggerSetup(logfilepath=None)

    # Multiple usage cases - to show that logging setup is reused without re-instantiating the LoggerSetup class
    program_logic_one()
    program_logic_two()
