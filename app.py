from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

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
    dbc.Container(
        class_name="m-0 p-0",
        children=[dbc.Row(
            class_name="mt-2",
            children=[
                dbc.Col(
                    width=2,
                    class_name="bg-light",
                    style={"minHeight":"95vh"},
                    children=[
                        html.H4("Specs", className="ms-4"),
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
        )])

]


@callback(

    Output('graph-content', 'figure'),
    Input('spec_name', 'value')
)
def update_graph(value):
    if value == "FOV":
        df_melted = specs.melt(id_vars=['product_id', 'product_name'], value_vars=['FOV_vertical', 'FOV_horizontal'],
                               var_name='FOV', value_name='Value')

        fig = px.bar(df_melted, x='product_name', y='Value', color='FOV',
                      barmode='group')
        fig.update_layout(plot_bgcolor ="white")

        return fig

    df = specs[['product_id', 'product_name', value]]
    fig= px.bar(df, x='product_name', y=value)
    fig.update_layout(plot_bgcolor="white")
    return fig


if __name__ == '__main__':
    app.run(debug=True)
