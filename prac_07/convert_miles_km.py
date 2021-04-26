"""Practical 07 - Do from scratch exercises.
Kivy GUI program to convert miles to kilometres.
Zeb del Rosario, Bachelor of IT
Started 26/04/2021"""
from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Zeb del Rosario"

MILES_TO_KM_RATE = 1.609323529411765


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy app that converts miles to km."""
    message = StringProperty()

    def build(self):
        """Build the app using Kivy."""
        Window.size = (500, 350)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, input_number):
        """Convert miles to kilometres, output result to output label."""
        miles = self.convert_to_number(input_number)
        miles *= MILES_TO_KM_RATE
        self.message = self.root.ids.output_label.text = f"{miles:.3f}"

    def handle_increment(self, input_number, increment_value):
        """Increase/decrease current entry by 1."""
        input_value = self.convert_to_number(input_number)
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
