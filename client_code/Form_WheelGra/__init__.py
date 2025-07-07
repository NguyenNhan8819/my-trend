from ._anvil_designer import Form_WheelGraTemplate
from anvil import *
import plotly.graph_objects as go

class Form_WheelGra(Form_WheelGraTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # fig =go.Figure(go.Sunburst(
    #   labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    #   parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    #   values=[None, 14, 12, 10, 2, 6, 6, 4, 4],
    #   branchvalues="total"
    # ))
    # fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

    # self.plot_1.figure = fig
    # Gốc dữ liệu
    labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
    values = [10, 14, 12, 10, 2, 6, 6, 4, 4]
    colors = [
      "lightblue",   # Eve
      "orange",      # Cain
      "green",       # Seth
      "red",         # Enos
      "pink",        # Noam
      "yellow",      # Abel
      "purple",      # Awan
      "brown",       # Enoch
      "gray"         # Azura
    ]

    # Dịch thứ tự 1 lát (đây là ví dụ đơn giản, bạn có thể xoay nhiều hơn)
    rotate_by = 1  # số bước lát muốn xoay
    # n = len(labels)

    # Xoay song song 3 danh sách
    labels_rot = labels[rotate_by:] + labels[:rotate_by]
    parents_rot = parents[rotate_by:] + parents[:rotate_by]
    values_rot = values[rotate_by:] + values[:rotate_by]

    fig = go.Figure(go.Sunburst(
      labels=labels_rot,
      parents=parents_rot,
      values=values_rot,
      marker=dict(colors=colors), 
      hole=0.05
    ))
    fig.update_layout(margin=dict(t=10, l=10, r=10, b=10))
    self.plot_1.figure = fig