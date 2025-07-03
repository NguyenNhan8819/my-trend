import anvil.server
import datetime
import plotly.graph_objects as go

def init_figure():
  # Khởi tạo thời gian bắt đầu
  start_time = datetime.datetime(2025, 1, 1, 0, 0, 0)

  # Tạo figure trống
  fig = go.Figure()

  # Cập nhật layout
  fig.update_layout(
    title={
      'text': "Giản đồ máy rang",
      'font': {'size': 13}
    },
    xaxis={
      'title': {
        'text': "Thời gian (phút:giây)",
        'font': {'size': 13}
      },
      'range': [
        start_time,
        start_time + datetime.timedelta(minutes=30)
      ],
      'dtick': 120000,  # mỗi 1 phút = 60.000 ms (do type=date)
      'tickformat': '%M',
      'tickwidth': 1,
      'type': 'date',
    },
    yaxis={
      'title': {
        'text': "Nhiệt độ (°C)",
        'font': {'size': 13}
      },
      'range': [0, 500],
      'dtick': 50,
      'fixedrange': True,
      'tickwidth': 1,
      'showline':True,
      
    },
    yaxis2={  # Trục Y bên phải
    'title': "Tốc độ quạt (%)",
    'range': [0, 100],
    'overlaying': 'y',
    'side': 'right',
    'showgrid': False,
    'showline': True
    }
  )

  return fig