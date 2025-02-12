from dash import Dash, html, dcc
from dash import Dash, html, dcc, Input, Output, callback
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
    ),

    html.Br(),

    html.Label('Input your mood:'),
    dcc.Input(id='input_widget'),
    # html.Div(dcc.Input(id='input_widget'))
    html.Label('Output: '),
    html.Div(id='output_area')
])


# Server side callbacks/reactivity
# ...


def update_example(input_value):
    return input_value

@callback(
    Output(component_id='output_area', component_property='children'),
    Input(component_id='input_widget', component_property='value')
)
def update_output(input_value):
    # The if-clause is optional and prevents the function from running until some text is entered
    if input_value:
        # We can use an fstring to have some constant text in the output
        return f'You are {input_value}!'
    else:
        return None

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
