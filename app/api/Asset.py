from importlib.abc import TraversableResources
from app.extension import es
from flask import current_app as app
import json

class Asset:
    ## Save vao elasticsearch. Thanh cong tra lai True, that bai tra lai False
    ## 
    @staticmethod
    def save(assettype, data):
        ret = False
        index_name=app.config['ELASTICSEARCH_DATAINDEX']
        json_data = json.loads(data)
        json_data['assettype'] = assettype
        resp = es.index(index=index_name,document=json_data)
        if resp['result'] == "created":
            ret = True
        return ret

    ##
    ## Tim cac document co gia tri chinh xac dinh o mot so truong
    ##
    @staticmethod
    def searchExtractField(searchDict):
        
        list_condition=[]
        for key, value in searchDict.items():
            txt_condition= '{"match": { "' + key + '":"' + value  + '" }}'
            list_condition.append(txt_condition) 

        condition = ",".join(list_condition)
        
        txt_query='''{
                "bool": {
                    "must": [ ''' + str(condition) + ''']
                }
        }'''
        
        #print(txt_query)
        index_name=app.config['ELASTICSEARCH_DATAINDEX']
        resp = es.search(index=index_name, query=json.loads(txt_query))
        return resp 

class IPaddressAsset(Asset):

    #Kiem tra xem ip da ton tai tren he thong chua
    @staticmethod
    def isExist(ipaddress):
        exist_flag = False
        searchDict={
            "assettype":"ipaddress",
            "ipaddress": ipaddress
        }
        resp = Asset.searchExtractField(searchDict)
        if int(resp['hits']['total']['value']) >= 1:
            exist_flag = True
        return exist_flag


class NetworkAsset(Asset):
    
    #Kiem tra xem network da ton tai tren he thong chua
    @staticmethod
    def isExist(cidr):
        exist_flag = False
        searchDict={
            "assettype":"network",
            "cidr": cidr
        }
        resp = Asset.searchExtractField(searchDict)
        if int(resp['hits']['total']['value']) >= 1:
            exist_flag = True
        return exist_flag

class SystemAsset(Asset):
    
    #Kiem tra xem network da ton tai tren he thong chua
    @staticmethod
    def isExist(name):
        exist_flag = False
        searchDict={
            "assettype":"system",
            "name": name
        }
        resp = Asset.searchExtractField(searchDict)
        if int(resp['hits']['total']['value']) >= 1:
            exist_flag = True
        return exist_flag


     