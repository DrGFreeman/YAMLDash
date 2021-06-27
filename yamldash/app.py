from multiprocessing import cpu_count
import webbrowser

import dash

from yamldash.layout import layout
from yamldash.layout import theme

ascii_title = r"""
 __     __      __  __ _      _____            _
 \ \   / //\   |  \/  | |    |  __ \          | |
  \ \_/ //  \  | \  / | |    | |  | | __ _ ___| |__
   \   // /\ \ | |\/| | |    | |  | |/ _` / __| '_ \
    | |/ ____ \| |  | | |____| |__| | (_| \__ \ | | |
    |_/_/    \_\_|  |_|______|_____/ \__,_|___/_| |_|

"""

app = dash.Dash(
    __name__,
    external_stylesheets=[
        theme,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    ],
)

wsgi_app = app.server

app.title = "YAMLDash - Interactive YAML Validation"

app.layout = layout

from yamldash import callbacks  # noqa: E402, F401


def run_debug():
    app.run_server(debug=True)


def run():

    print(ascii_title)
    webbrowser.open("127.0.0.1:8080", new=2)

    try:
        import waitress

        print("Listening on 127.0.0.1:8080.")
        print("Press CTRL-C to stop.")

        waitress.serve(wsgi_app, listen="127.0.0.1:8080", threads=cpu_count())

    except ModuleNotFoundError:
        print("Waitress server not found (use 'pip install waitress' to install it)")
        print("Defaulting to Flask development server.\n")

        app.run_server(port=8080)
