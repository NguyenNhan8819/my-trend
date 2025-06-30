from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data_points = []       # Lưu (phút, nhiệt độ)
    self.total_seconds = 0      # Đếm thời gian thực tế
    self.temp_box.text = 30
    self.timer_1.interval = 0


  def start_button_click(self, **event_args):
    """Khi nhấn nút Bắt đầu"""
    self.timer_1.interval = 5
    self.start_button.enabled = False  # Không cho nhấn lại
    self.status_label.text = "Đang ghi dữ liệu mỗi 5 giây..."


  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    """Chạy mỗi 5 giây"""
    try:
      temp = float(self.temp_box.text)
      minute = self.total_seconds // 5
      self.data_points.append((minute, temp))

      self.total_seconds += 5
      self.update_plot()
      self.status_label.text = f"Đã thêm {temp}°C tại phút {minute}"

    except ValueError:
      self.status_label.text = "Không ghi: nhiệt độ chưa hợp lệ"
  def update_plot(self):
    if not self.data_points:
      self.plot_1.figure = go.Figure()
      return
    times = [t[0] for t in self.data_points]
    temps = [t[1] for t in self.data_points]
    # fig = go.Figure()
    data =  go.Scatter(
      x=times,
      y=temps,
      mode='lines',
      name="Nhiệt độ"
    )
    # fig.update_layout(
    #   title="Trend nhiệt độ mỗi 5 giây",
    #   xaxis_title="Thời gian (phút)",
    #   yaxis_title="Nhiệt độ (°C)",
    #   template="plotly_white"
    # )
    self.plot_1.data = data
    print (self.data_points)
    