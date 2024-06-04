from LoggerSetup import LoggerSetup
from sub1 import program_logic_one
from sub2 import program_logic_two

if __name__ == "__main__":
    # Initial setup - only do once
    LoggerSetup(logfilepath=None)

    # Multiple usage cases
    program_logic_one()
    program_logic_two()
