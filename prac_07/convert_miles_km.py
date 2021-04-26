"""Practical 07 - Do from scratch exercises.
Kivy GUI program to convert miles to kilometres.
Zeb del Rosario, Bachelor of IT
Started 26/04/2021"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = "Zeb del Rosario"


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy app that converts miles to km."""
    def build(self):
        """Build the app using Kivy."""
        Window.size = (500, 350)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        """Convert miles to kilometres, output result to """
        value *= 1.609323529411765  # convert mile to km
        self.root.ids.output_label.text = f"{value:.3f}"
        print(f"{value:.3f}")


ConvertMilesToKmApp().run()
