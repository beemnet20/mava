import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from components.sidebar import sidebar

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
app.title = "MAVA"
server = app.server




app.layout = html.Div([
    dbc.Navbar(
        children=[
            dbc.Container(
                children=[
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src="/assets/images/logo.svg", height="30px")),
                                dbc.Col(dbc.NavbarBrand("MAVA", class_name="ms-2")),
                            ],
                            align="center",
                            class_name="g-0",
                        ),
                        href="#",
                        style={"textDecoration": "none"}
                    ),
                ],
                class_name="ms-2 justify-content-start",
            )
        ],
        color="primary",
        dark=True
    ),
    dbc.Row(
        class_name = "w-100",
        children = [dbc.Col(sidebar(), width=2), dbc.Col(dash.page_container, width=10)]
    )
])



if __name__ == '__main__':
    app.run(debug=True)
