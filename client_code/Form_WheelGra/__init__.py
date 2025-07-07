from ._anvil_designer import Form_WheelGraTemplate
from anvil import *
import plotly.graph_objects as go

class Form_WheelGra(Form_WheelGraTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Tạo biểu đồ Sunburst với màu theo từng vòng
    fig = go.Figure(go.Sunburst(
      labels=[
        "Root",             # Vòng 1
        "Module A", "Module B",     # Vòng 2
        "Sensor A1", "Sensor A2", "Sensor B1", "Sensor B2"  # Vòng 3
      ],
      parents=[
        "",          # Root
        "Root", "Root",      # Vòng 2
        "Module A", "Module A", "Module B", "Module B"  # Vòng 3
      ],
      values=[
        10,        # Root (10%)
        15, 15,    # Vòng 2
        20, 10,    # A1 + A2
        20, 10     # B1 + B2
      ],
      branchvalues="total",
      marker=dict(colors=[
        "royalblue",      # Root
        "orange", "orange",  # Vòng 2
        "red", "red", "red", "red"  # Vòng 3
      ])
    ))

    fig.update_layout(
      margin=dict(t=10, l=10, r=10, b=10)
    )

    # Gán biểu đồ cho Plot component trong Anvil
    self.plot_1.figure = fig