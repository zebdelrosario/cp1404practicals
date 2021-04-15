"""CP1404 Practical 06: Classes - Intermediate exercises."""


class ProgrammingLanguage:
    def __init__(self, language="", typing="", reflection="", year=0):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.language}, {self.typing}, {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        return False
