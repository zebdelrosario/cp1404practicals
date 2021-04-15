"""Emails: Stores users' emails and names in a dictionary."""


def main():
    """Prompt user for email and corresponding name"""
    name_email_dict = {}
    is_blank_email = False
    while not is_blank_email:
        email = input("Email: ")
        if email == "":
            is_blank_email = True
        else:
            name = determine_name(email)
            confirm_name = input(f"Is your name {name}? (Y/n) ").lower()
            if confirm_name == "n" or confirm_name == "no":
                name = input("Name: ").title()
            name_email_dict[name] = email
    for name, email in name_email_dict.items():
        print(f"{name} ({email})")


def determine_name(email):
    """Determine name from an email address."""
    name = email[:email.find("@")]
    return name.title()


main()
