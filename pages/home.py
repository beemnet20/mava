import pandas as pd
import dash
from dash import html
import dash_bootstrap_components as dbc
from components.productsCardDisplay import productsCardDisplay
import os

script_dir = os.path.dirname(__file__)
data_dir = os.path.join(script_dir, '..', 'data')
file_path = os.path.join(data_dir, 'product_specs.csv')
specs = pd.read_csv(file_path)
df = specs[["product_name", "img_src", "description", "starting_price", "href"]]
productsList = df.to_dict(orient='records')

dash.register_page(__name__, path="/")

layout = html.Div(
    [productsCardDisplay(productsList),
     dbc.Alert("I do not own these products, this is only for practicing developing with plotly dash framework", color="primary")
     ]
)
