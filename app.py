from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

specs = pd.read_csv("./data/product_specs.csv")

units_dict = dict(starting_price="dollars", DRAM="GB",
                  base_storage="GB", display_resolution_PPI="Pixels per inch",
                  display_resolution_PPD="pixels per degree",
                  refresh_rate="Hz", color_gamut="% of sRGB",
                  battery_run_time="hours",
                  FOV="degrees"
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
                        dbc.Col(dbc.NavbarBrand("MAVA", class_name="ms-2")),
                    ],
                    align="center",
                    class_name="g-0",
                ),
                href="#",
                style={"textDecoration": "none"}
            )],
            class_name="ms-2",
        )],
        color="primary",
        dark=True
    ),

    dbc.Row(
        class_name="mt-2",
        children=[
            dbc.Col(
                width=2,
                children=[
                    html.H3("Specs"),
                    dbc.RadioItems(
                        id="spec_name",
                        class_name="p-0",
                        options=[{"label": x if x.isupper() else x.replace("_", " ").capitalize(), "value": x} for x
                                 in
                                 units_dict.keys()],
                        value="starting_price",  # Default selected value
                        inline=False,  # Stacks vertically
                        label_class_name="btn rounded-0 w-100",
                        label_checked_class_name="bg-primary text-white",
                        input_class_name="d-none",
                        label_style={"textAlign": "left"}
                    ),
                ]
            ),
            dbc.Col(
                width=10,
                children=[
                    dcc.Graph(id='graph-content')
                ]
            )

        ]
    )

]


@callback(

    Output('graph-content', 'figure'),
    Input('spec_name', 'value')
)
def update_graph(value):
    dff = specs[['product_id', 'product_name', value]]

    return px.bar(dff, x='product_name', y=value)


if __name__ == '__main__':
    app.run(debug=True)
