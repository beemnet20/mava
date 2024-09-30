import dash
from dash import html
import dash_bootstrap_components as dbc


def sidebar():
    return html.Div(
        [html.Br(),
        dbc.Nav(
            [
                dbc.NavLink(
                    html.Div(page["name"], className="ms-2"),
                    href=page["path"],
                    active="exact",
                    class_name="rounded-0"
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            class_name="bg-light",
            style={"minHeight":"85vh"}
        )]
    )