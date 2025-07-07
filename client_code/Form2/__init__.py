from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.color_picker_1.visible = False
    self.color_picker_1.set_event_handler('x-color_changed', self._on_color_changed)

  def button_show_click(self, **event_args):
    self.color_picker_1.visible = not self.color_picker_1.visible

  def _on_color_changed(self, **event_args):
    color = event_args['color']
    self.label_result.text = f"Bạn chọn: {color}"
    self.label_result.foreground = color
    self.color_picker_1.visible = False