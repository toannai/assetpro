"""General page routes."""
from flask import Blueprint

# Blueprint Configuration
blueprint  = Blueprint(
    "api", __name__, template_folder="templates", static_folder="static"
)



#
@blueprint.route("/api/asset", methods=["GET"])
def createAsset():
    return "createAsset"