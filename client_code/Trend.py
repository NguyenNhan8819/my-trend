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
        'tickmode':'array',
        'tickvals':self.tick_vals,
        'ticktext':self.tick_vals,
        'tickwidth':1
      },
    yaxis={
      'title': {
        'text': "Nhiệt độ C" ,
        'font': {'size' : 13},
      },
      'range': [0, 500],
      'fixedrange':True,
      'tickwidth':1
    }      
  )
  return fig