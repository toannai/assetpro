"""General page routes."""
from flask import Blueprint

# Blueprint Configuration
blueprint  = Blueprint(
    "home", __name__, template_folder="templates", static_folder="static"
)


@blueprint.route("/", methods=["GET"])
def home():
    return "Home bluesprint page"