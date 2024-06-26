'''
tail.py - a python implementation of the unix tail utility.

Commandline Arguments:
    #1 (required) - the filename of the file to read
    #2 (optional) - the number of lines to read

Algorithm:
    - Open file and read the file as lines into a list
    - Print out the last N lines of the list
'''


import sys


# Default number of lines to read if argument is not specified
_DEFAULT_LINES = 10


def read_all_the_lines(filename, length):
    '''
    Open and read the last N number of lines

    Args:
        filename (str): The name of the file to open and read
        length (int): The number of lines to read from the file

    Returns:
        last_lines (list): The last N number of lines read from the file
    '''

    last_lines = []

    # Open the filename provided by user; if not present exit the program
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            last_lines = lines[-length:]
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    return last_lines


def main():
    '''
    The main function to collect user command line arguments
    to output the last N lines of the file
    '''

    # Capture required first system argument; if not present exit the program
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please provide a filename.")
        sys.exit(1)

    # Capture optional second system argument; if not present use _LAST_LINES
    try:
        results = read_all_the_lines(filename, int(sys.argv[2]))
    except IndexError:
        results = read_all_the_lines(filename, _DEFAULT_LINES)

    for result in results:
        print(result.strip())


if __name__ == "__main__":
    main()
