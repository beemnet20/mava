import dash
from dash import html, callback, Input, Output, State
from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc

links = [
    dbc.NavLink("GitHub", href="https://github.com/beemnet20/mava"),
]


def sidebar():
    return html.Div(
        id="sidebar-container",
        style = {"height":"100vh", "backgroundColor":"#f8f9fa"},
        children=[
            html.Div(
                className="d-flex flex-row-reverse bg-primary border-light border-end",
                children=[dbc.Button(id="sidebar-toggler", children=html.I(className="fa-solid fa-bars"),
                                     class_name="sidebar-toggler bg-primary text-white border-0",
                                     style={"width":"50px"}
                                     )],
                style={"height":"50px"}
            ),
            html.Br(),
            dbc.Nav(
                id="sidebar-content",
                children=[
                             dbc.NavLink(
                                 html.Div(page["name"], className="ms-2"),
                                 href=page["path"],
                                 active="exact",
                                 class_name="rounded-0"
                             )
                             for page in dash.page_registry.values()
                         ] + links,
                vertical=True,
                pills=True
            )]
    )


@callback(
    Output("sidebar-container", "className"),
    Output("sidebar-content", "class_name"),
    Input("sidebar-toggler", "n_clicks"),
    State("sidebar-container", "className"),
)
def toggleSidebar(n_clicks, current_classes):
    if n_clicks is None:
        raise PreventUpdate
    if current_classes is not None and "collapsed" in current_classes:
        return "", ""
    return "collapsed", "collapsed"
