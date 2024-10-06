import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from components.sidebar import sidebar
from components.navbar import navbar

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME], use_pages=True)
app.title = "MAVA"
server = app.server

app.layout = html.Div([
    html.Div(
        className="d-flex",
        children=[html.Div(sidebar(), className=""), html.Div([navbar(),html.Div( dash.page_container, className="m-2")], className="w-100")]
    )
])

if __name__ == '__main__':
    app.run(debug=True)
