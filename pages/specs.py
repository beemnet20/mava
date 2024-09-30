import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import os
from components.radioButtonGroup import radioButtonGroup

script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir, '..', 'data')
file_path = os.path.join(data_dir, 'product_specs.csv')
specs = pd.read_csv(file_path)

dash.register_page(__name__)

units_dict = dict(DRAM="GB",
                  base_storage="GB", display_resolution_PPI="Pixels per inch",
                  display_resolution_PPD="pixels per degree",
                  refresh_rate="Hz", color_gamut="% of sRGB",
                  battery_run_time="hours",
                  FOV="degrees"
                  )


def format_var_str(input_str):
    formatted_str = input_str.replace("_", " ")
    words = formatted_str.split()
    if not words[0].isupper():
        words[0] = words[0].capitalize()
    return " ".join(words)


radio_options = [{"label": format_var_str(x), "value": x} for x in units_dict.keys()]

layout = dbc.Container(
    class_name="m-0 p-0",
    children=[dbc.Row(
        class_name="mt-2",
        children=[

            radioButtonGroup(id="spec_name", options=radio_options),
            dbc.Row(
                children=[
                    dcc.Graph(id='graph-content')
                ]
            )

        ]
    )])


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
        fig.update_layout(plot_bgcolor="white")

        return fig

    df = specs[['product_id', 'product_name', value]]
    fig = px.bar(df, x='product_name', y=value, text=value)
    fig.update_layout(plot_bgcolor="white", xaxis_title=None, yaxis_title=None,
                      title=f"{format_var_str(value)} ({units_dict[value]})")
    return fig
