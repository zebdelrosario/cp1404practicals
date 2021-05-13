"""CP1404 - Prac 09
Sort files program
Author: Zeb del Rosario
Start date: 13/05/2021
"""
import os

ROOT_DIRECTORY = os.getcwd()


def main():
    """Creat subdirectories for file extensions and move corresponding files into those directories."""
    print(f"Current directory: {ROOT_DIRECTORY}")  # this assumes the program is inside the directory to be changed
    print("-" * 50, f"\nFiles inside {ROOT_DIRECTORY}:")
    # for file in os.listdir():
    #     print(file)
    file_extension = determine_file_extensions(ROOT_DIRECTORY)
    print(file_extension)


def determine_file_extensions(root_directory):
    """Determine what file extensions are inside current folder."""
    for root, subdirectories, files in os.walk(root_directory):
        file_paths = [root + "\\" + file for file in files]  # create path to file
        file_root_extensions = [os.path.splitext(file_path) for file_path in file_paths]  # split file path from ext
        file_extensions = [file_extension for root, file_extension in file_root_extensions]  # store ext in list
        return file_extensions


main()
