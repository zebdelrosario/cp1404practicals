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
    file_paths = determine_file_paths(ROOT_DIRECTORY)
    file_extensions = determine_file_extensions(file_paths)
    print(file_extensions)


def determine_file_paths(root_directory):
    """Determine correct path for files inside root directory."""
    for root, subdirectories, files in os.walk(root_directory):
        file_paths = [root + "\\" + file for file in files]  # create path to file
        return file_paths


def determine_file_extensions(file_paths):
    """Determine what file extensions are inside current folder."""
    roots_extensions = [os.path.splitext(file_path) for file_path in file_paths]  # split file path from ext
    file_extensions = [file_extension for root, file_extension in roots_extensions]  # store ext in list
    for file_extension in file_extensions:  # remove multiples of extension
        if file_extensions.count(file_extension) > 1:
            file_extensions.remove(file_extension)
    return file_extensions


main()
