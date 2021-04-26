"""
Practical 07 - Do from scratch exercises.
Kivy GUI program to create dynamic labels based on a list of names.
Zeb del Rosario, Bachelor of IT
Started 26/04/2021"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window


__author__ = "Zeb del Rosario"

NAMES = ["Tryhard Scrub", "Budget Tryhard Scrub", "Smallest Cash Cow", "Anime Simp", "King Crimson", "Bad DBD Player"]


class DynamicLabels(App):
    def build(self):
        """Build the Kivy file for the app."""
        Window.size = (500, 350)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in NAMES:
            temp_button = Button(text=name)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicLabels().run()
