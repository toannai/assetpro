"""General page routes."""
from flask import Blueprint, request, Response
import json
from app.api.Asset import Asset


# Blueprint Configuration
blueprint  = Blueprint(
    "api", __name__, template_folder="templates", static_folder="static"
)


# api create asset
@blueprint.route("/api/asset", methods=["POST"])
def createAsset():
    type= request.form.get("type")
    data = request.form.get("data")
    
    result = "false" # Luu ket qua them vao
    msg = "" #Message tra ve
    status_code = 200

    if (type is not None) and (data is not None):
        ######Them ip vao csdl
        if type == "ipaddress":
            createIPAddress(data)
            result = "success"
            msg = "Add ip success"
            status_code = 200
        ######Them network vao csdl
        elif type == "network":
            createNetworkAddress(data)
            result = "success"
            msg = "Add network success"
            status_code = 200
        ##### Them asset khong thanh cong
        else:
            result = "false"
            msg = "Asset Type Unsupported"
            status_code = 400
    else:
        result = "false"
        msg = "Invalid input data"
        status_code = 400
    
    resp_text = str({'result':result, 'msg':msg})

    return Response(resp_text, status=status_code, mimetype='application/json')


## Them Dia chi ip vao csdl
def createIPAddress(data):
    ## them truong asset type vao object
    json_data = json.loads(data)
    json_data["assettype"]="ipaddress"
    print(json_data)
    resp = es.index(index="test-index", document=json_data)
    print(resp['result'])
## Them network vao csdl
def createNetworkAddress(data):
    pass
