from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Change output_label's display to match input_name."""
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_fields(self):
        """Clear current values of input_name and output_label."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
