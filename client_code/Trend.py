import anvil.server
import datetime
import plotly.graph_objects as go

def init_figure():
  # Khởi tạo thời gian bắt đầu
  start_time = datetime.datetime(2025, 1, 1, 0, 0, 0)

  # Tạo figure trống
  fig = go.Figure(
    data=[
      go.Scatter(x=[], y=[], mode="lines", name='BT'),
      go.Scatter(x=[], y=[], mode="lines", name='Delta BT', yaxis="y2")
    ],
    layout=go.Layout(
    title={
      'text': "Giản đồ máy rang",
      'font': {'size': 25}
    },
    xaxis={
      'title': {
        'text': "Thời gian (phút)",
        'font': {'size': 13}
      },
      'range': [
        start_time,
        start_time + datetime.timedelta(minutes=30)
      ],
      'dtick': 120000,  # mỗi 2 phút = 120.000 ms (do type=date)
      'tickformat': '%M:%S',
      'tickwidth': 1,
      'type': 'date',
    },
    yaxis={
      'title': {
        'text': "Nhiệt độ (°C)",
        'font': {'size': 13}
      },
      'range': [0, 300],
      'dtick': 50,
      'tickwidth': 1,
      'showline':True,
    },
    yaxis2={  # Trục Y bên phải
    'title': {
      'text': "Độ tăng nhiệt độ C/phút",
      'font': {'size': 13}
    },
    'range': [0, 50],
    'dtick': 10,
    'tickwidth': 1,
    'overlaying': 'y',
    'side': 'right',
    'showgrid': False,
    'showline': True
    },
    legend=dict(
    x=0.95,           # Gần sát phải, nhưng không tràn qua trục y2
    y=1.15,              # Trên cùng
    xanchor='right',  # Căn phải
    yanchor='top',
    orientation='h'   # Giữ chiều dọc
    ),
    annotations=[]
  )
  )
  return fig