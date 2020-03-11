from src.apicall import api_call
from src.input import  get_inputs
from src.elastic_search import *
import os
from elasticsearch import Elasticsearch;


if __name__=="__main__":
    inputs = get_inputs()
    data=api_call(inputs)

    es = Elasticsearch()
    mapping = open("es_mapping.txt","r").read()
    es.indices.create(index="opcv",body=mapping)
    push_data(es,data)
    





