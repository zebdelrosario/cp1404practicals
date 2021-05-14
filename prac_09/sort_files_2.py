"""CP1404 - Prac 09
Sort files 2 program
Author: Zeb del Rosario
Start date: 13/05/2021
"""

import os
import shutil

ROOT_DIRECTORY = os.getcwd() + "\\" + "FilesToSort"  # force cwd to be set to "FilesToSort"


def main():
    """Sort files v2; sort files based on user input."""
    categories_extensions_dic = {}
    print(f"Root directory: {ROOT_DIRECTORY}")
    print("-" * 50)
    source_file_paths = determine_file_paths(ROOT_DIRECTORY)
    file_extensions = determine_file_extensions(source_file_paths)
    print(source_file_paths, "\n")
    for index, file_extension in enumerate(file_extensions):
        file_category_name = input(f"What category would you like to sort {file_extension} files into? ")
        destination_directory_path = ROOT_DIRECTORY + "\\" + file_category_name
        create_new_directory(ROOT_DIRECTORY, file_category_name)
        for source_file_path in source_file_paths:
            if source_file_path.endswith(file_extension):
                move_files_to_directory(source_file_path, destination_directory_path)


def move_files_to_directory(source_file_path, destination_directory_path):
    """Move files from given root to destination directory."""
    try:
        shutil.move(source_file_path, destination_directory_path)
    except FileExistsError:
        pass


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
    file_extensions = []
    roots_extensions = [os.path.splitext(file_path) for file_path in file_paths]  # split file path from ext
    raw_file_extensions = [file_extension.strip(".") for root, file_extension in roots_extensions]  # store ext in list
    for raw_file_extension in raw_file_extensions:
        if raw_file_extension not in file_extensions:
            file_extensions.append(raw_file_extension)
    return file_extensions


main()
