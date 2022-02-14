import sys


def parsing_command_line_parameters():
    """
    The function parses the command line parameters and returns the parameter with index 2.
    :return: The command line parameter with index 2
    """
    return sys.argv[2]


if __name__ == '__main__':
    parsing_command_line_parameters()
