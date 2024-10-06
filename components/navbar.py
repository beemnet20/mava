import dash_bootstrap_components as dbc
from dash import html


def navbar():
    return dbc.Navbar(
        dbc.Container(
            class_name="ms-0",
            children=[html.Div(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand(html.Span(
                            [html.Img(src="../assets/images/logo.svg", className="mx-2", height="30px"), "MAVA"]),
                                                class_name="ms-2", href="/")),
                    ],
                    align="center",
                    class_name="g-0",
                ),
                style={"textDecoration": "none"}
            )]),
        color="primary",
        dark=True,
        style={"height": "50px"}
    )
