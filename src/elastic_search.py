from elasticsearch import Elasticsearch

def prep_data(data: list) -> dict:
    result=[]
    for record in data:
        temp =dict(record)
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
    
