"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    underscored_name = filename.replace(" ", "_").replace(".TXT", ".txt").strip(".txt")
    if "_" not in underscored_name:  # if filename is not separated
        separated_filename = "".join(" " + char if char.isupper() else char for char in underscored_name).strip(" ").split(" ")
        fixed_name = "_".join(separated_filename)
    else:  # if filename is separated in any way
        fixed_name = underscored_name.title()
    return fixed_name + ".txt"


main()
