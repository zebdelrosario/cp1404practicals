"""CP1404 - Prac 09
Sort files program
Author: Zeb del Rosario
Start date: 13/05/2021
"""
import os
import shutil

ROOT_DIRECTORY = os.getcwd() + "\\" + "FilesToSort"  # force cwd to be set to "FilesToSort"


def main():
    """Creat subdirectories for file extensions and move corresponding files into those directories."""
    print(f"Current directory: {ROOT_DIRECTORY}")  # this assumes the program is inside the directory to be changed
    print("-" * 50, f"\nFiles inside {ROOT_DIRECTORY}:")
    source_file_paths = determine_file_paths(ROOT_DIRECTORY)
    file_extensions = determine_file_extensions(source_file_paths)
    for file_extension in file_extensions:
        create_new_directory(ROOT_DIRECTORY, file_extension)
    for source_file_path in source_file_paths:
        move_files_to_directory(source_file_path, file_extensions)
    print(file_extensions)


def move_files_to_directory(source_file_path, file_extensions):
    """Move files from given root to destination directory."""
    for index, file_extension in enumerate(file_extensions):
        if source_file_path.endswith(file_extension):
            destination_directory = ROOT_DIRECTORY + f"\\{file_extension}"
            try:
                shutil.move(source_file_path, destination_directory)
            except FileExistsError:
                pass


def create_new_directory(root_directory, file_extension):
    """Create a new directory named after given argument inside given file path."""
    try:
        os.mkdir(root_directory + "\\" + file_extension)
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
