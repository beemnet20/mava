import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/beemnet20/mava")),
    ],
    brand=html.A(
        dbc.Row(
            [
                dbc.Col(html.Img(src="../assets/images/logo.svg", height="30px")),
                dbc.Col(dbc.NavbarBrand("MAVA", class_name="ms-2")),
            ],
            align="center",
            class_name="g-0",
        ),
        href="#",
        style={"textDecoration": "none"}
    ),
    brand_href="/",
    color="primary",
    dark=True,
)
