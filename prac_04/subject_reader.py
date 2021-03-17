"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        subject_data.append(parts)
        print(subject_data)
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()
    return subject_data


def display_subject_details(data):
    """Display subject details from a list of data."""
    for item in data:
        subject = item[0]
        teacher = item[1]
        number_of_students = item[2]
        print("{} is taught by {:12} and has {:3} students".format(subject, teacher, number_of_students))


main()
