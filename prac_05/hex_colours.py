"""Hex colours program: Enter a colour name and receive its corresponding hex colour."""
COLOUR_HEX_DICT = {"firebrick": "#b22222", "DodgerBlue1": "#1e90ff", "DeepPink1": "#ff1493", "DarkSlateBlue": "#483d8b",
                   "DarkOrange": "	#ff8c00", "DarkOliveGreen1": "#caff70", "DarkGoldenrod": "#b8860b",
                   "coral": "#ff7f50",
                   "black": "#000000", "AntiqueWhite": "#faebd7"}


def main():
    """Hex colour translator: enter a valid colour name to see its hex value."""
    print("Please enter a number from the following list to see its hex value:")
    display_valid_colours(COLOUR_HEX_DICT)
    selected_colour = get_valid_colour(">>> ", COLOUR_HEX_DICT)
    print(COLOUR_HEX_DICT[selected_colour])


def display_valid_colours(dictionary):
    """Display a list of valid colours."""
    for name in dictionary:
        print(f"{name.title()}")


def get_valid_colour(prompt, dictionary):
    """Prompt user for colour until a valid entry is made."""
    is_valid_colour = False
    while not is_valid_colour:
        try:
            colour = str(input(prompt)).lower()
            if colour not in dictionary:
                print(f"Please enter a valid color from the list provided:")
            else:
                return colour
        except ValueError:
            print("Enter a valid colour")


main()
