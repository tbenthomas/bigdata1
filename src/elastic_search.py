from elasticsearch import Elasticsearch
from datetime import datetime
def prep_data(data: list) -> dict:
    result=[]
    for record in data:
        temp =dict(record)

        date=list(map(int,temp["issue_date"].split('/')))
        temp["issue_date"]=datetime(month=date[0],day=date[1],year=date[2])
        
        entry = {'index': temp['plate'],
                  'doc_type':'ticket',
                  'body': temp
                  }
        result.append(entry)
    return result
        
def push_data(es: Elasticsearch,data: list):

    records=prep_data(data)

    for record in records:    
        res = es.index(index="opcv",doc_type=record['doc_type'],body=record['body'])
        print(res['result'])
    
