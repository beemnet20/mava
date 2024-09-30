from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

specs = pd.read_csv("./data/product_specs.csv")


units_dict = dict(starting_price="dollars", DRAM="GB",
                  base_storage="GB", display_resolution_PPI="Pixels per inch",
                  display_resolution_PPD="pixels per degree",
                  refresh_rate="Hz", color_gamut="% of sRGB",
                  battery_run_time = "hours",
                  FOV_vertical = "degrees",
                  FOV_horizontal = "degrees"
                  )

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "MAVA"
server = app.server

app.layout = [

    dbc.Navbar(
        children=[dbc.Row(
            children=[html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/images/logo.svg", height="30px")),
                        dbc.Col(dbc.NavbarBrand("MAVA", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"}
            )],
            className="ms-2",
        )],
        color="primary",
        dark=True
    ),
    dcc.Dropdown(list(units_dict.keys()), "starting_price", id="dropdown-selection"),
    dcc.Graph(id='graph-content')
]


@callback(

    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = specs[['product_id','product_name',value]]

    return px.bar(dff, x='product_name', y=value)


if __name__ == '__main__':
    app.run(debug=True)
