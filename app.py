from typing import Optional

from flask import Flask, render_template, request

app = Flask(__name__)


def _parse_int(value: Optional[str], fallback: int) -> int:
    """Convert user input to int while keeping a sensible default on errors."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


@app.route("/", methods=["GET", "POST"])
def home():
    """Render the multiplication table trainer view."""
    default_number = 2
    default_upto = 10

    if request.method == "POST":
        number = _parse_int(request.form.get("number"), default_number)
        upto = _parse_int(request.form.get("upto"), default_upto)
    else:
        number = _parse_int(request.args.get("number"), default_number)
        upto = _parse_int(request.args.get("upto"), default_upto)

    number = max(number, 1)
    upto = max(upto, 1)

    table_rows = [
        {
            "base": number,
            "multiplier": multiplier,
            "product": number * multiplier,
        }
        for multiplier in range(1, upto + 1)
    ]

    return render_template(
        "table.html",
        number=number,
        upto=upto,
        table_rows=table_rows,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
