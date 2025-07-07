from ._anvil_designer import ColorPickerTemplateTemplate
from anvil import *
import anvil.server
import anvil.js

class ColorPickerTemplate(ColorPickerTemplateTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    node = self.dom_nodes['color_input']

    # Setter property ban đầu
    node.value = self.initial_color

    # Đăng ký sự kiện thay đổi
    node.addEventListener('input', self._on_color)

  @property
  def initial_color(self):
    return getattr(self, '_initial_color', '#000000')

  @initial_color.setter
  def initial_color(self, value):
    self._initial_color = value
    # Trả giá trị này về input
    if 'color_input' in self.dom_nodes:
      self.dom_nodes['color_input'].value = value

  def _on_color(self, e):
    self.raise_event('x-color_changed', color=e.target.value)
