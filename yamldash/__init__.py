import dash

from yamldash.layout import layout
from yamldash.layout import theme


app = dash.Dash(__name__, external_stylesheets=[theme])

app.title = "YAMLDash - Interactive YAML Validation"

app.layout = layout

import yamldash.callbacks  # noqa: E402, F401
