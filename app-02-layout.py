from dash import Dash, html
from dash import dcc # dash core component

import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Initiatlize the app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('Hello Dash'),
    html.P('Dash converts Python classes into HTML'),
    html.P("This conversion happens behind the scenes by Dash's JavaScript front-end"),

    dcc.Markdown('''
    # Hello Dash

    Dash converts Python classes into HTML

    This conversion happens behind the scenes by Dash's JavaScript front-end
''')
])

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.run()
