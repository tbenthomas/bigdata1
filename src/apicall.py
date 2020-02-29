from sodapy import Socrata
import json

def api_call(inputs: dict):
    #create api client
    client=Socrata(
        "data.cityofnewyork.us",
        inputs['APP_KEY'])
        
    #either store api calls to file or print to terminal
    if "output" in inputs.keys():
        try:
            with open(inputs['output'], 'w') as fout:
                for i in range(inputs['num_pages']):
                    data_get=client.get("nc67-uf89",limit=inputs['page_size'],offset=inputs['page_size']*i)
                    json.dump(data_get,fout)
        except FileNotFoundError as err:
            print("\nPlease enter a valid file name with extension, or leave out --output to print to terminal")
    else:
        for i in range(inputs['num_pages']):
            print(client.get("nc67-uf89",limit=inputs['page_size'],offset=inputs['page_size']*i))
                
        print("No output file specified, outputting to terminal")
    
    

    
