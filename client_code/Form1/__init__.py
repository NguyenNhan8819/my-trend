from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
from datetime import datetime, timedelta
from .. import Trend
import json

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.start_time = datetime(2025, 1, 1, 0, 0, 0) # Khởi tạo thời gian, ngày tháng năm chủ yếu đủ định dạng
    self.data_points = [] # Tạo một list lưu trữ dữ liệu nhiệt độ theo thời gian
    self.annotations = [] # Tạo list lưu chú thích
    self.temp_box.text = 30 # Gán giá trị nhiệt độ ban đầu
    self.deltaBT_box.text = 20 # Gán giá trị nhiệt độ ban đầu
    # Tạo figure và gán data rỗng
    # self.plot_1.figure = Trend.init_figure()
    # self.plot_1.data = [go.Scatter(x=[], y=[], mode="lines+markers", name='Nhiệt độ BT'),
    #                     go.Scatter(x=[],y=[],yaxis='y2',showlegend=True,mode='lines', name='Delta BT',line=dict(width=2))
    # ]
    # Khởi tạo figure với 2 trace
    self.plot_1.figure = Trend.init_figure()
    
    self.timer_1.interval = 0 # Ban đầu timer chưa hoạt động

  def start_button_click(self, **event_args):
    self.timer_1.interval = 5    # Ghi mỗi 5 giây
    self.start_button.enabled = False
    self.status_label.text = "Đang ghi dữ liệu mỗi 5 giây..."
    self.now = datetime.now ()

  def timer_1_tick(self, **event_args):
    try:
      temp = float(self.temp_box.text)
      dBT = float(self.deltaBT_box.text)
      elapsed = datetime.now() - self.now
      minutes, seconds = divmod(elapsed.seconds, 60)
      time_string = f"{minutes:02}:{seconds:02}"
      self.data_points.append((time_string, temp, dBT))
      self.update_plot_latest(self.data_points)
      self.plot_1.figure.update_layout(annotations=self.annotations)
      self.plot_1.figure = self.plot_1.figure
      
      self.status_label.text = f"Ghi nhận nhiệt độ {temp}°C và deltaBT {dBT} tại phút {time_string}"
      print (elapsed.seconds)
      print ('y là',self.plot_1.figure.data[0].y)
    except ValueError:
      self.status_label.text = "Không ghi: nhiệt độ chưa hợp lệ"
      
  def update_plot_latest(self, dataList):
    self.dataList = dataList
    if not self.dataList:
      return
    # Lấy điểm dữ liệu mới nhất
    time_str, value, dBT = self.dataList[-1]
    minutes, seconds = map(int, time_str.split(":"))
    dt = self.start_time + timedelta(minutes=minutes, seconds=seconds)
    # Cập nhật trace đầu tiên (trace nhiệt độ)
    # trace1 = self.plot_1.data[0]
    # trace2 = self.plot_1.data[1]
    # trace1.x.append(dt)
    # trace2.x.append(dt)
    # trace1.y.append(value)
    # trace2.y.append(dBT)
    # self.plot_1.data = [trace1,trace2]
    # # Cập nhật trace mà không gán lại .data
    self.plot_1.figure.data[0].x.append(dt)
    self.plot_1.figure.data[0].y.append(value)
    self.plot_1.figure.data[1].x.append(dt)
    self.plot_1.figure.data[1].y.append(dBT)
    
  def add_annotation(self, dataList, text):
    if not dataList:
      return
    # Lấy điểm dữ liệu mới nhất
    time_str, value, dBT = dataList[-1]
    minutes, seconds = map(int, time_str.split(":"))
    dti = self.start_time + timedelta(minutes=minutes, seconds=seconds)
    self.annotations.append(dict(
      x=dti,
      y=value,
      xref="x",
      yref="y",
      text=text,
      showarrow=True,
      arrowhead=2,
      ax=30,
      ay=30
    ))
    print ("chú thích là", text)
    print ("value là", value)
    print ("dt là", dti)

  def update_annotation_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anns = list (self.plot_1.figure.layout.annotations)+[self.add_annotation (self.data_points, "Điểm bắt đầu")]
    self.plot_1.figure.update_layout(annotations=anns)
    self.plot_1.figure = self.plot_1.figure
    
  
    



