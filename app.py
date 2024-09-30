import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from components.sidebar import sidebar
from components.navbar import navbar

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
app.title = "MAVA"
server = app.server

app.layout = html.Div([
    navbar,
    dbc.Row(
        class_name="w-100",
        children=[dbc.Col(sidebar(), width=2), dbc.Col(dash.page_container, width=10)]
    )
])

if __name__ == '__main__':
    app.run(debug=True)
