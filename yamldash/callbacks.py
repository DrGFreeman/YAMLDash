from dash.dependencies import Input
from dash.dependencies import Output

import jsonschema
import yaml

from yamldash import app


@app.callback([Output("yaml_text", "className"),
               Output("yaml_feedback", "children")],
              [Input("schema_text", "value"),
               Input("yaml_text", "value")])
def validate_yaml(schema_text, yaml_text):
    class_name = "form-control"
    has_schema = False

    if schema_text != "" and schema_text is not None:
        try:
            schema_dict = yaml.safe_load(schema_text)
            has_schema = True
        except Exception:
            print("Error parsing schema")
            pass

    try:
        if yaml_text != "" and yaml_text is not None:
            yaml_dict = yaml.safe_load(yaml_text)
        else:
            return (class_name, "")
    except Exception as e:
        print(e)
        return (
            class_name + " is-invalid",
            f"YAML ParsingError: {e}"
        )

    if yaml_dict is not None:
        if has_schema:
            try:
                jsonschema.validate(yaml_dict, schema_dict)
                return (class_name + " is-valid", "")
            except jsonschema.exceptions.ValidationError as e:
                print("Invalid, schema ValidationError", e)
                return (
                    class_name + " is-invalid",
                    f"Schema ValidationError: {e}"
                )
        else:
            return (class_name + " is-valid", "")
    else:
        return (class_name, "")
