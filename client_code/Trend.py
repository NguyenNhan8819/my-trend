import anvil.server
import plotly.graph_objects as go
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .. import Module1

def init_trend (self, **properties):
  fig = go.Figure()
  fig.update_layout (
      title= {
        'text': "Giản đồ máy rang" ,
        'font': {'size' : 13},
      },
      xaxis={
        'range': [0, 500]
      },
      yaxis={
        'range': [0, 500]
      }
      
      
  )
  return fig