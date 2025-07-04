from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
from datetime import datetime, timedelta
from .. import Trend

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.start_time = datetime(2025, 1, 1, 0, 0, 0) # Khởi tạo thời gian
    self.data_points = [] # Tạo một list lưu trữ dữ liệu nhiệt độ theo thời gian
    self.temp_box.text = 30 # Gán giá trị nhiệt độ ban đầu
    # Tạo figure và gán data rỗng
    self.plot_1.figure = Trend.init_figure()
    self.plot_1.data = [go.Scatter(x=[], y=[], mode='lines', name='Nhiệt độ'),
                        go.Scatter(x=[],y=[],yaxis='y2',showlegend=False,
                                    hoverinfo='skip',
                                    mode='lines',
                                    line=dict(width=0)
                                  )]
    
    self.time = 0
    self.time_list = "00:00"
    self.timer_1.interval = 0 # Ban đầu timer chưa hoạt động
    self.timer_2.interval = 0 # Ban đầu timer chưa hoạt động

  def start_button_click(self, **event_args):
    self.timer_1.interval = 5    # Ghi mỗi 5 giây
    self.timer_2.interval = 1    # Cập nhật thời gian mỗi 1 giây
    self.start_button.enabled = False
    self.status_label.text = "Đang ghi dữ liệu mỗi 5 giây..."

  def timer_1_tick(self, **event_args):
    try:
      temp = float(self.temp_box.text)
      minute = self.time_list
      self.data_points.append((minute, temp))
      self.update_plot()
      self.status_label.text = f"Đã thêm {temp}°C tại phút {minute}"
    except ValueError:
      self.status_label.text = "Không ghi: nhiệt độ chưa hợp lệ"

  def timer_2_tick(self, **event_args):
    self.time += 1
    t = timedelta(seconds=self.time)
    minutes, seconds = divmod(t.seconds, 60)
    self.time_list = f"{minutes:02}:{seconds:02}"

  def update_plot(self):
    x_data = []
    y_data = []

    for time_str, value in self.data_points:
      minutes, seconds = map(int, time_str.split(":"))
      dt = self.start_time + timedelta(minutes=minutes, seconds=seconds)
      x_data.append(dt)
      y_data.append(value)
    self.plot_1.data = [go.Scatter(x=x_data, y=y_data, mode='lines', name='Nhiệt độ'),
                        go.Scatter(x=[],y=[],yaxis='y2',showlegend=False,
                                   hoverinfo='skip',
                                   mode='lines',
                                   line=dict(width=0)
                        )]
    print ("X data la ", x_data)
    print(self.data_points)



