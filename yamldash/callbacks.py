from dash.dependencies import Input
from dash.dependencies import Output
import jsonschema
import yaml

from yamldash import app


@app.callback(
    [
        Output("schema", "data"),
        Output("schema_text", "className"),
        Output("schema_feedback", "children"),
        Output("schema_feedback", "className"),
    ],
    [Input("schema_text", "value")],
)
def validate_schema(schema_text):
    class_name = "form-control"

    if schema_text != "" and schema_text is not None:
        try:
            schema_dict = yaml.safe_load(schema_text)
            jsonschema.validate({}, schema_dict)
        except jsonschema.exceptions.SchemaError as e:
            return (
                None,
                class_name + " is-invalid",
                f"Invalid Schema: {e}",
                "invalid-feedback",
            )
        except jsonschema.ValidationError:
            return (
                schema_dict,
                class_name + " is-valid",
                "Valid Schema",
                "valid-feedback",
            )
        except Exception as e:
            return (
                None,
                class_name + " is-invalid",
                f"YAML ParsingError: {e}",
                "invalid-feedback",
            )

    return (None, class_name, "", "")


@app.callback(
    [Output("yaml_text", "className"), Output("yaml_feedback", "children")],
    [Input("schema", "data"), Input("yaml_text", "value")],
)
def validate_yaml(schema, yaml_text):
    class_name = "form-control"

    try:
        if yaml_text != "" and yaml_text is not None:
            yaml_dict = yaml.safe_load(yaml_text)
        else:
            return class_name, ""
    except Exception as e:
        return (class_name + " is-invalid", f"YAML ParsingError: {e}")

    if yaml_dict is not None:
        if schema is not None:
            try:
                jsonschema.validate(yaml_dict, schema)
                return class_name + " is-valid", ""
            except jsonschema.exceptions.ValidationError as e:
                return (class_name + " is-invalid", f"Schema ValidationError: {e}")
        else:
            return class_name + " is-valid", ""
    else:
        return class_name, ""
