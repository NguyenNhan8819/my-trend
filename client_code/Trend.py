import anvil.server
import plotly.graph_objects as go
from datetime import datetime, timedelta

# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1

def init_figure (self, **properties):
  tick_seconds = list(range(0, 21 * 60, 120))  # mỗi 5 phút
  self.tick_vals = [f"{s//60:02}:{s%60:02}" for s in tick_seconds]
  print (self.tick_vals)
  fig = go.Figure()
  fig.update_layout (
      title= {
        'text': "Giản đồ máy rang" ,
        'font': {'size' : 13},
      },
      xaxis={
        'title': {
          'text': "Thời gian phút" ,
          'font': {'size' : 13},
        },
        'range': [0, 500],
        'dtick':50,
        'tickwidth':1
        # 'tickmode':'array',
        # 'tickvals':self.tick_vals,
        # 'ticktext':self.tick_vals,
        # 'tickheigh':5,
        # 'tickangle':45
      },
    yaxis={
      'title': {
        'text': "Nhiệt độ C" ,
        'font': {'size' : 13},
      },
      'range': [0, 500],
      'dtick':50,
      'fixedrange':True,
      'tickwidth':1
    }      
  )
  return fig

def dual_axis_figure():
  fig = go.Figure()

  # Dữ liệu trục Y trái (Nhiệt độ)
  fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[100, 130, 160, 180, 210, 230],
    name="Nhiệt độ (°C)",
    line=dict(color='orange'),
    yaxis="y"
  ))

  # Dữ liệu trục Y phải (RoR)
  fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[5, 6, 5.5, 4.5, 3, 2],
    name="RoR (°C/min)",
    line=dict(color='cyan', dash='dot'),
    yaxis="y2"  # ✅ gán trace này vào trục Y thứ 2
  ))

  fig.update_layout(
    title="Giản đồ máy rang với 2 trục Y",
    xaxis=dict(
      title="Thời gian (phút)",
      dtick=1
    ),
    yaxis=dict(
      title="Nhiệt độ (°C)",
      range=[0, 250],
      dtick=50
    ),
    yaxis2=dict(
      title="RoR (°C/min)",
      overlaying='y',
      side='right',
      range=[0, 10],
      dtick=2,
      showgrid=False
    ),
    legend=dict(x=0.01, y=0.99),
    height=500,
    width=800
  )

  return fig