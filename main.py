import argparse
from pathlib import Path
from data_manipulator import DataManipulator

if __name__ == '__main__':
    # __name__ is the name of this file  - python assigning this in start
    # this function executes only when this specific file is instantiated
    # and not when other python file called this file
    try:

        # Using argparse package to run from terminal and pass the src_path and dest_path from user
        # no matter where this app runs
        parser = argparse.ArgumentParser(description='App for parsing json files')
        parser.add_argument('src_path', type=str, help='source path of the json file')
        parser.add_argument('dest_path', type=str, help='destination path of the json file')

        args = parser.parse_args()

        src_path = args.src_path
        dest_path = args.dest_path

        data_manipulator = DataManipulator(Path(src_path))
        data_manipulator.process_data()
        data_manipulator.save_json(Path(dest_path))

    except Exception as e:
        print(f'General error: {e.__class__}')  # print the name of the specific exception class name
