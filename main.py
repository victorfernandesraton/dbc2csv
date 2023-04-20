

import argparse
import os
import logging

from dbc2csv import *


def main():
    parser = argparse.ArgumentParser(description='dbc2csv converter')

    parser.add_argument(
        'path', type=str, help='the relative path to check and run recursive transformation')
    
    args = parser.parse_args()
   
    handler = Dbc2bfc(logging.getLogger())

    # Check if the path exists
    if os.path.exists(args.path):
        print(f"The path '{args.path}' exists.")
        handler.run(args.path)
    else:
        print(f"The path '{args.path}' does not exist.")


if __name__ == '__main__':
    main()
