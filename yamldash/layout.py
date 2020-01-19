from pathlib import Path

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

SRC_URL = "https://github.com/DrGFreeman/YAMLDash"

theme = dbc.themes.UNITED

defaults_path = Path(__file__).parent.joinpath('defaults')
print(defaults_path.as_posix())

with open(defaults_path.joinpath('default_schema.yaml'), 'r') as f:
    default_schema = f.read()

with open(defaults_path.joinpath('default.yaml'), 'r') as f:
    default_yaml = f.read()

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Source Code",
                href=SRC_URL,
                external_link=True,
            )
        ),
    ],
    brand="YAMLDash",
    brand_href="#",
    color="primary",
    dark=True,
)

yaml_col = dbc.Col(
    [
        html.H2(
            "YAML",
            className="mt-3"
        ),
        dbc.Textarea(
            id="yaml_text",
            className="form-control",
            placeholder="Enter the YAML content here...",
            value=default_yaml,
            rows=20,
            spellCheck=False,
            wrap=False,
        ),
        html.Div(
            "",
            id="yaml_feedback",
            className="invalid-feedback",
        ),
    ],
    width=12,
    lg=6,
)

schema_col = dbc.Col(
    [
        html.H2(
            "Schema",
            id="schema-h2",
            className="mt-3"
        ),
        dbc.Tooltip(
            "A schema allows validation of the YAML data "
            "against specific requirements.",
            target="schema-h2",
            placement="left",
        ),
        dbc.Textarea(
            id="schema_text",
            placeholder="Enter an optional validation schema here...",
            value=default_schema,
            rows=20,
            spellCheck=False,
            wrap=False,
        ),
        dcc.Store(
            id="schema",
            storage_type="memory",
        ),
        html.Div(
            "",
            id="schema_feedback",
            className="invalid-feedback",
        ),
    ],
    width=12,
    lg=6,
)

footer = html.Div(
    [
        html.Hr(
            className="mb-3"
        ),
        html.P(
            [
                html.Small(
                    "Ⓒ 2020, Julien de la Bruère-Terreault (DrGFreeman)."
                ),
                html.Br(),
                html.Small(
                    [
                        html.A(
                            "MIT License",
                            href=SRC_URL + "/blob/master/LICENSE",
                        ),
                        ". Source code available at ",
                        html.A(
                            SRC_URL,
                            href=SRC_URL,
                        ),
                        ".",
                    ]
                )
            ],
            className="text-center text-muted"
        ),
    ],
    className="mt-4"
)

body = dbc.Container(
    children=[
        dbc.Row(
            [
                yaml_col,
                schema_col
            ],
        ),
        footer,
    ]
)

layout = html.Div([navbar, body])
