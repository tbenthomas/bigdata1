from sodapy import Socrata
import json

def api_call(inputs: dict):
    client=Socrata(
        "data.cityofnewyork.us",
        inputs['APP_KEY'])
    try:
        with open(inputs['output'], 'w') as fout:
            for i in range(inputs['num_pages']):
                data_get=client.get("nc67-uf89",limit=inputs['page_size'],offset=inputs['page_size']*i)
                json.dump(data_get,fout)
    except KeyError:
        print("Error: Please enter a file name with extension '.json'")
    

    
