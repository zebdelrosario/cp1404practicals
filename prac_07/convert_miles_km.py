"""Practical 07 - Do from scratch exercises.
Kivy GUI program to convert miles to kilometres.
Zeb del Rosario, Bachelor of IT
Started 26/04/2021"""
from kivy.app import App, StringProperty
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Zeb del Rosario"


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy app that converts miles to km."""
    message = StringProperty()

    def build(self):
        """Build the app using Kivy."""
        Window.size = (500, 350)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        """Convert miles to kilometres, output result to """
        value *= 1.609323529411765  # convert mile to km
        self.message = self.root.ids.output_label.text = f"{value:.3f}"

    def handle_increment(self, increment_value):
        """Increase/decrease current entry by 1."""
        input_value = int(self.root.ids.input_number.text)
        input_value = input_value + int(increment_value)
        self.root.ids.input_number.text = str(input_value)

    @staticmethod
    def convert_to_number(text):
        """Convert text to 0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesToKmApp().run()
