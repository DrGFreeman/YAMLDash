from pathlib import Path

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

SRC_URL = "https://github.com/DrGFreeman/YAMLDash"
YAML_REF_URL = "https://yaml.org/spec/1.2/spec.html"
SCHEMA_REF_URL = "https://json-schema.org/draft/2019-09/json-schema-validation.html"

theme = dbc.themes.UNITED

defaults_path = Path(__file__).parent.joinpath("defaults")

with open(defaults_path.joinpath("default_schema.yaml"), "r") as f:
    default_schema = f.read()

with open(defaults_path.joinpath("default.yaml"), "r") as f:
    default_yaml = f.read()

navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(dbc.NavLink("YAML Reference", href=YAML_REF_URL, target="_blank")),
        dbc.NavItem(dbc.NavLink("Schema Reference", href=SCHEMA_REF_URL, target="_blank")),
        dbc.NavItem(
            dbc.NavLink(
                ["Source Code ", html.I(className="fa fa-lg fa-github")],
                href=SRC_URL,
                target="_blank",
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
        html.H2("YAML", className="mt-3"),
        dbc.Textarea(
            id="yaml_text",
            className="form-control",
            placeholder="Enter the YAML content here...",
            value=default_yaml,
            rows=20,
            spellCheck=False,
            wrap="off",
        ),
        html.Div("", id="yaml_feedback", className="invalid-feedback"),
    ],
    width=12,
    lg=6,
)

schema_col = dbc.Col(
    [
        html.H2("Schema", id="schema-h2", className="mt-3"),
        dbc.Tooltip(
            "A schema allows validation of the YAML data " "against specific requirements.",
            target="schema-h2",
            placement="left",
        ),
        dbc.Textarea(
            id="schema_text",
            placeholder="Enter an optional validation schema here...",
            value=default_schema,
            rows=20,
            spellCheck=False,
            wrap="off",
        ),
        dcc.Store(id="schema", storage_type="memory",),
        html.Div("", id="schema_feedback", className="invalid-feedback"),
    ],
    width=12,
    lg=6,
)

footer = html.Div(
    [
        html.Hr(className="mb-3"),
        html.P(
            [
                html.Small(
                    [
                        "Ⓒ 2020, Julien de la Bruère-Terreault (DrGFreeman). ",
                        html.A("MIT License", href=SRC_URL + "/blob/master/LICENSE"),
                        ".",
                    ]
                ),
            ],
            className="text-center text-muted",
        ),
    ],
    className="mt-4",
)

body = dbc.Container(children=[dbc.Row([yaml_col, schema_col],), footer])

layout = html.Div([navbar, body])
