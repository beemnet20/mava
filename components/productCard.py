import dash_bootstrap_components as dbc
from dash import html

def productCard(img_src, product_name, description,starting_price, href):
    return dbc.Card(
        [
            dbc.CardImg(src=img_src, top=True),
            dbc.CardBody(
                [
                    html.H4(product_name, className="card-title"),
                    html.P(
                        description,
                        className="card-text",
                    ),
                    html.P(
                        "Starting at",
                        className="text-secondary my-1"
                    ),
                    html.Strong(
                        f"${starting_price} USD"
                    ),
                    dbc.Button("Learn more", color="primary", href=href, class_name="d-block my-2", style={"borderRadius":"23px"}),
                ]
            ),
        ],
        class_name="w-100 border-0"
    )