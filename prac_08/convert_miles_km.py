from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


MILES_TO_KM_CONST = 1.609


class ConvertMilesKm(App):
    def build(self):
        Window.size = (500, 400)
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        try:
            result = float(value) * MILES_TO_KM_CONST
            self.root.ids.km_label.text = str(result)
        except ValueError:
            self.root.ids.km_label.text = '0'

    def increment_input(self, value):
        try:
            result = float(self.root.ids.input_value.text) + value
            self.root.ids.input_value.text = str(result)
        except ValueError:
            self.root.ids.input_value.text = str(value)


ConvertMilesKm().run()
