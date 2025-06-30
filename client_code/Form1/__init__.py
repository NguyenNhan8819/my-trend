from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data_points = []       # Lưu (phút, nhiệt độ)
    self.total_seconds = 0      # Đếm thời gian thực tế
    self.temp_box.text = 30

    self.timer_1.enabled = False  # Chưa bắt đầu

  def start_button_click(self, **event_args):
    """Khi nhấn nút Bắt đầu"""
    self.timer_1.enabled = True
    self.start_button.enabled = False  # Không cho nhấn lại
    self.status_label.text = "Đang ghi dữ liệu mỗi 5 giây..."

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    """Chạy mỗi 5 giây"""
    try:
      temp = float(self.temp_box.text)
      minute = self.total_seconds // 60
      self.data_points.append((minute, temp))

      self.total_seconds += 5
      self.update_plot()
      self.status_label.text = f"Đã thêm {temp}°C tại phút {minute}"

    except ValueError:
      self.status_label.text = "Không ghi: nhiệt độ chưa hợp lệ"

    self.plot_1.figure = fig