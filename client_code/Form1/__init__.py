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
    self.annotations = [] # Tạo list lưu chú thích
    self.temp_box.text = 30 # Gán giá trị nhiệt độ ban đầu
    self.deltaBT_box.text = 20 # Gán giá trị nhiệt độ ban đầu
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
      self.plot_1.figure = self.plot_1.figure
      self.status_label.text = f"Ghi nhận nhiệt độ {temp}°C và deltaBT {dBT} tại phút {time_string}"
    except ValueError:
      self.status_label.text = "Không ghi: nhiệt độ chưa hợp lệ"

  def update_plot_latest(self, dataList):
    self.dataList = dataList
    if not self.dataList:
      return
    # Lấy điểm dữ liệu mới nhất
    time_str, bt, dBT = self.dataList[-1]
    minutes, seconds = map(int, time_str.split(":"))
    dt = self.start_time + timedelta(minutes=minutes, seconds=seconds)
    # # Cập nhật trace mà không gán lại .data
    self.plot_1.figure.data[0].x.append(dt)
    self.plot_1.figure.data[0].y.append(bt)
    self.plot_1.figure.data[1].x.append(dt)
    self.plot_1.figure.data[1].y.append(dBT)

  def add_annotation(self, dataList, text):
    if not dataList:
      return
    # Lấy điểm dữ liệu mới nhất
    time_str, bt, dBT = dataList[-1]
    minutes, seconds = map(int, time_str.split(":"))
    dt = self.start_time + timedelta(minutes=minutes, seconds=seconds)
    self.annotations.append(dict(
      x=dt,y=bt,xref="x",yref="y",
      text=f'{text} {time_str}',              
      font=dict(size=10,color="red"),                
      arrowwidth=1,showarrow=True,arrowhead=0,ax=30,ay=30
    ))
    self.annotations.append(dict(
      x=dt,y=bt,xref="x",yref="y",
      text=f'{bt}',              
      font=dict(size=10,color="red"),                
      arrowwidth=1,showarrow=True,arrowhead=0,ax=30,ay=-30
    ))
  def charge_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'Charge')
    self.plot_1.layout.annotations = self.annotations
    self.charge_button.enabled = False

  def dryend_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'DE')
    self.plot_1.layout.annotations = self.annotations
    self.dryend_button.enabled = False

  def tp_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'TP')
    self.plot_1.layout.annotations = self.annotations
    self.tp_button.enabled = False

  def fcStart_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'FcS')
    self.plot_1.layout.annotations = self.annotations
    self.fcStart_button.enabled = False

  def fcEnd_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'FcE')
    self.plot_1.layout.annotations = self.annotations
    self.fcEnd_button.enabled = False

  def scStart_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'ScS')
    self.plot_1.layout.annotations = self.annotations
    self.scStart_button.enabled = False

  def scEnd_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'ScE')
    self.plot_1.layout.annotations = self.annotations
    self.scEnd_button.enabled = False

  def drop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.add_annotation (self.data_points, 'Drop')
    self.plot_1.layout.annotations = self.annotations
    self.drop_button.enabled = False

  def plot_1_hover(self, points, **event_args):
    """This method is called when a data point is hovered."""

    i = points
    # print(f"Bạn vừa hover vào điểm: ({self.plot_1.figure.data[0].x[i]}, {self.plot_1.figure.data[0].y[i]})")
    print (i)







