"""CP1404 Practical 06: Classes - Intermediate exercises."""
from programming_language import ProgrammingLanguage


def main():
    """Display a list of programming languages that are dynamically typed."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.language)


main()
