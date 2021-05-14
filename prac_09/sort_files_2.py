"""CP1404 - Prac 09
Sort files 2 program
Author: Zeb del Rosario
Start date: 13/05/2021
"""

import os

ROOT_DIRECTORY = os.getcwd() + "\\" + "FilesToSort"  # force cwd to be set to "FilesToSort"


def main():
    """Sort files v2; sort files based on user input."""
    print(f"Root directory: {ROOT_DIRECTORY}")
    print("-" * 50)
    source_file_paths = determine_file_paths(ROOT_DIRECTORY)
    file_extensions = determine_file_extensions(source_file_paths)
    for file_extension in file_extensions:
        destination_directory_name = input(f"What category would you like to sort {file_extension} files into? ")
        destination_directory_path = ROOT_DIRECTORY + "\\" + destination_directory_name
        create_new_directory(ROOT_DIRECTORY, destination_directory_name)
        print(destination_directory_path)


def create_new_directory(root_directory, new_directory_name):
    """Create a new directory named after given argument inside given file path."""
    try:
        os.mkdir(root_directory + "\\" + new_directory_name)
    except FileExistsError:
        print(f"Directory already exists; ignoring create command..")
        pass


def determine_file_paths(root_directory):
    """Determine correct path for files inside root directory."""
    for root, subdirectories, files in os.walk(root_directory):
        file_paths = [root + "\\" + file for file in files]  # create path to file
        return file_paths


def determine_file_extensions(file_paths):
    """Split file extensions from files inside given file paths."""
    roots_extensions = [os.path.splitext(file_path) for file_path in file_paths]  # split file path from ext
    file_extensions = [file_extension.strip(".") for root, file_extension in roots_extensions]  # store ext in list
    for file_extension in file_extensions:  # remove multiples of extension
        if file_extensions.count(file_extension) > 1:
            file_extensions.remove(file_extension)
    return file_extensions


main()
