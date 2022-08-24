from os import environ
from elasticsearch import Elasticsearch


#es_url = environ.get("ES_URI")
es_url = "http://192.168.150.131:9200"
es = Elasticsearch(es_url)

