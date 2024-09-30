import dash_bootstrap_components as dbc
from dash import html
from components.productCard import productCard


def productsCardDisplay(productsList):
    return dbc.Container(class_name="my-2", children=[html.H1("Product lineup"), dbc.Row(
        children=[
            dbc.Col(productCard(product["img_src"], product["product_name"], product["description"],
                                product["starting_price"], product["href"])) for product in productsList]

    )])
