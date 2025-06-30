import anvil.server
import plotly.graph_objects as go

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def update_plot(self):
  if not self.data_points:
    self.plot_1.figure = go.Figure()
    return
  times = [t[0] for t in self.data_points]
  temps = [t[1] for t in self.data_points]
  fig = go.Figure()
  fig.add_trace( go.Scatter(
    x=times,
    y=temps,
    mode='lines+markers',
    name="Nhiệt độ"
  ))
  fig.update_layout(
    title="Trend nhiệt độ mỗi 5 giây",
    xaxis_title="Thời gian (phút)",
    yaxis_title="Nhiệt độ (°C)",
    template="plotly_white"
  )