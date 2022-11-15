from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jeff1", "Jeff2", "Jeff3", "Jeff4", "Jeff5"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
