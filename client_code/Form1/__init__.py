from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
from datetime import datetime, timedelta
from .. import Trend


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    fig = Trend.init_figure(self)
    tick_vals = fig.layout['xaxis']['tickvals']
    self.plot_1.data = go.Scatter(
      x=tick_vals,
      y=[0,100,200,300,100,200,100,400,300,100,150],
      mode='lines',
      name='Dữ liệu trống'
    )
    print (tick_vals)
    # Any code you write here will run before the form opens.

  #   self.data_points = []       # Lưu (phút, nhiệt độ)
  #   self.temp_box.text = 30
  #   self.timer_1.interval = 0
  #   self.timer_2.interval = 0
  #   self.time=0
  #   self.plot_trend()

    

  # def start_button_click(self, **event_args):
  #   """Khi nhấn nút Bắt đầu"""
  #   self.timer_1.interval = 5
  #   self.timer_2.interval = 1
  #   self.start_button.enabled = False  # Không cho nhấn lại
  #   self.status_label.text = "Đang ghi dữ liệu mỗi 5 giây..."

  # def timer_1_tick(self, **event_args):
  #   """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
  #   """Chạy mỗi 5 giây"""
    
  #   try:
  #     temp = float(self.temp_box.text)
  #     minute = self.time_list
  #     self.data_points.append((minute, temp))
  #     self.update_plot()
  #     self.status_label.text = f"Đã thêm {temp}°C tại phút {minute}"
  #   except ValueError:
  #     self.status_label.text = "Không ghi: nhiệt độ chưa hợp lệ"
  # def update_plot(self):
  #   if not self.data_points:
  #     self.plot_1.figure = go.Figure()
  #     return
  #   times = [t[0] for t in self.data_points]
  #   temps = [t[1] for t in self.data_points]
  #   # fig = go.Figure()
  #   data =  go.Scatter(
  #     x=times,
  #     y=temps,
  #     mode='lines',
  #     name="Nhiệt độ"
  #   )
  #   # fig.update_layout(
  #   #   title="Trend nhiệt độ mỗi 5 giây",
  #   #   xaxis_title="Thời gian (phút)",
  #   #   yaxis_title="Nhiệt độ (°C)",
  #   #   template="plotly_white"
  #   # )
  #   # self.plot_1.data = data
  #   print (self.data_points)

  # def timer_2_tick(self, **event_args): 
  #   self.time +=1
  #   t = timedelta(seconds=self.time)
  #   minutes, seconds = divmod(t.seconds, 60)
  #   self.time_list = f"{minutes:02}:{seconds:02}"
  # def plot_trend(self):
  #   # Tạo danh sách thời gian từ 00:00 đến 24:00 với bước mỗi 15 phút
  #   times = [datetime(2024, 1, 1, 0, 0) + timedelta(seconds=10 * i) for i in range(10)]
  #   print (times)

  #   # Dữ liệu nhiệt độ giả lập (hoặc bạn có thể lấy từ nguồn thực)
  #   temps = [100 + (i % 10) * 10 for i in range(len(times))]  # ví dụ: 100, 110, ...

  #   # Tạo biểu đồ
  #   fig = go.Figure(
  #     data = [go.Scatter(
  #       x=[t.strftime("%H:%M") for t in times],  # hiển thị giờ:phút
  #       y=temps,
  #       mode="lines+markers",
  #       name="Nhiệt độ"
  #     )]
  #   )
  #   # Cấu hình trục
  #   fig.update_layout(
  #     title="Biểu đồ nhiệt độ theo thời gian",
  #     xaxis_title="Thời gian (giờ:phút)",
  #     yaxis_title="Nhiệt độ (°C)",
  #     xaxis=dict(
  #       tickangle=45,
  #       tickmode='auto',
  #       nticks=12,
  #       range=[0, len(times) - 1]
  #     ),
  #     yaxis=dict(range=[0, 500]),
  #     height=500
  #   )

  #   # Hiển thị biểu đồ
  #   self.plot_1.figure = fig
    


    