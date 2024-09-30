import dash_bootstrap_components as dbc


def radioButtonGroup(id, options):
    return dbc.RadioItems(
        id=id,
        class_name="radio-button-group bg-light p-0 my-1  mx-auto",
        options=options,
        value="DRAM",
        inline=True,
        label_class_name="btn btn-outline-primary",
        label_checked_class_name="bg-primary text-white",
    )
