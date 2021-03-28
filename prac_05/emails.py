"""Emails: Stores users' emails and names in a dictionary."""


def main():
    """Prompt user for email and corresponding name"""
    email = input("Email: ")
    name = determine_name(email)


def determine_name(email):
    """Determine name from an email address."""
    name = email[:email.find("@")]
    return name.title()


main()
