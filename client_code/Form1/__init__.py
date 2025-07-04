from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
from datetime import datetime, timedelta
from .. import Trend

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.start_time = datetime(2025, 1, 1, 0, 0, 0) # Khởi tạo thời gian, ngày tháng năm chủ yếu đủ định dạng
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
    
    self.timer_1.interval = 0 # Ban đầu timer chưa hoạt động

  def start_button_click(self, **event_args):
    self.timer_1.interval = 5    # Ghi mỗi 5 giây
    self.start_button.enabled = False
    self.status_label.text = "Đang ghi dữ liệu mỗi 5 giây..."
    self.now = datetime.now ()

  def timer_1_tick(self, **event_args):
    try:
      temp = float(self.temp_box.text)
      elapsed = datetime.now() - self.now
      minutes, seconds = divmod(elapsed.seconds, 60)
      time_string = f"{minutes:02}:{seconds:02}"
      self.data_points.append((time_string, temp))
      self.update_plot_latest()
      self.status_label.text = f"Đã thêm {temp}°C tại phút {time_string}"
      print (elapsed.seconds)
    except ValueError:
      self.status_label.text = "Không ghi: nhiệt độ chưa hợp lệ"

  def update_plot(self):
    x_data = []
    y_data = []

    for time_str, value in self.data_points:
      minutes, seconds = map(int, time_str.split(":"))
      dt = self.start_time +  timedelta(minutes=minutes, seconds=seconds)
      x_data.append(dt)
      y_data.append(value)
    self.plot_1.data = [go.Scatter(x=x_data, y=y_data, mode='lines', name='Nhiệt độ'),
                        go.Scatter(x=[],y=[],yaxis='y2',showlegend=False,
                                   hoverinfo='skip',
                                   mode='lines',
                                   line=dict(width=0)
                                  )
                        ]
    print ("X data la ", x_data)
    print(self.data_points)
    
  def update_plot_latest(self):
    if not self.data_points:
      return

    # Lấy điểm dữ liệu mới nhất
    time_str, value = self.data_points[-1]
    minutes, seconds = map(int, time_str.split(":"))
    dt = self.start_time + timedelta(minutes=minutes, seconds=seconds)

    # Nếu figure chưa có trace, khởi tạo nó
    if not self.plot_1.data:
      self.plot_1.data = [go.Scatter(x=[dt], y=[value], mode='lines', name='Nhiệt độ')]
      return

    # Cập nhật trace đầu tiên (trace nhiệt độ)
    trace1 = self.plot_1.data[0]
    trace2 = self.plot_1.data[1]
    trace1.x.append(dt)
    trace1.y.append(value)
    self.plot_1.data = [trace1,trace2]
    



