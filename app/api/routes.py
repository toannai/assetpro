"""General page routes."""
from codecs import charmap_build
from ipaddress import ip_address
from flask import Blueprint, request, Response
import json

from app.api.Asset import Asset,IPaddressAsset, NetworkAsset, SystemAsset


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
    status_code = 400

    if (type is not None) and (data is not None): #Kiem tra xem du lieu nguoi dung cung cap co du 2 truong khong
        ######Them ipaddress asset vao csdl
        if type == "ipaddress":
            if createIPAddress(data) == True: 
                ## Ket qua tra ve
                result = "success"
                msg = "Create ipadress success"
                status_code = 200
            else:
                ## Ket qua tra ve
                result = "fail"
                msg = "Create ipadress Failer. IP address existed on System"
                status_code = 400
        ######Them network asset vao csdl
        elif type == "network":
            if createNetwork(data) == True:
                ## Ket qua tra ve
                result = "success"
                msg = "Create network success"
                status_code = 200
            else:
                ## Ket qua tra ve
                result = "fail"
                msg = "Create network Failer. Network address existed on System"
                status_code = 400
        ######Them system asset vao csdl
        elif type == "system":
            if createSystem(data) == True:
                ## Ket qua tra ve
                result = "success"
                msg = "Create system success"
                status_code = 200
        
        ######Them device asset vao csdl
        elif type == "device":
            if createDevice(data) == True:
                ## Ket qua tra ve
                result = "success"
                msg = "Create device success"
                status_code = 200

        ######Them contact asset vao csdl
        elif type == "contact":
            if createContact(data) == True:
                ## Ket qua tra ve
                result = "success"
                msg = "device contact success"
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
    
    ### Ket qua tra ve cho nguoi goi api ####
    resp_text = str({'result':result, 'msg':msg})
    return Response(resp_text, status=status_code, mimetype='application/json')


## Them Dia chi ip vao csdl
def createIPAddress(data):
    pyObj = json.loads(data)
    ip_address = pyObj['ipaddress']
    
    if IPaddressAsset.isExist(ip_address) == False: #Kiem tra xem dia chi ip ton tai khong
        IPaddressAsset.save("ipaddress",data) #Them vao dia chi ip
        return True
    return False
## Them network vao csdl
def createNetwork(data):
    pyObj = json.loads(data)
    cidr = pyObj['cidr']
    if NetworkAsset.isExist(cidr) == False: #Kiem tra xem network ton tai chua
        NetworkAsset.save("network",data) #Them vao network
        return True
    return False

## Them He thong vao csdl
def createSystem(data):
    pyObj = json.loads(data)
    name = pyObj['name']
    if SystemAsset.isExist(name) == False: #Kiem tra xem ten he thong ton tai chua
        SystemAsset.save("name",data) #Them vao he thong
        return True
    return False

## Them Thiet bi vao csdl
def createDevice(data):
    a = Asset("device",data) #Khoi tao du lieu
    return a.save() # Ghi vao elasticsearch va tra lai ket qua

## Them Contact vao csdl
def createContact(data):
    a = Asset("contact",data) #Khoi tao du lieu
    return a.save() # Ghi vao elasticsearch va tra lai ket qua