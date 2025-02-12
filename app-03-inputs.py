from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.Label('My first slider'),
    dcc.Slider(min=0, max=5, value=2),

    html.Br(),  # Add whitespace; br = "break"
    html.Label('My first range slider'),
    dcc.RangeSlider(
        min=0,
        max=5,
        value=[1, 3],  # A list since it's a range slideer
        step=1,  # The step between values
        marks={0: '0', 5: '5'},  # The marks/labels on the slider
        tooltip={'always_visible': True, 'placement': 'bottom'}  # Show the current values
    ),

     html.Label('Dropdown'),
    dcc.Dropdown(
        options=['New York City', 'Montreal', 'San Francisco'],
        value='Montreal',
    ),

    html.Br(),
    # A widget with a self-explanatory placeholder does not need a label
    dcc.Dropdown(
        options=['New York City', 'Montreal', 'San Francisco'],
        multi=True,
        placeholder='Select multiple cities...'
    )
])

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
