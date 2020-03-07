from sodapy import Socrata
import json,sys
from multiprocessing import Pool,TimeoutError

def api_call(inputs: dict) -> list:
    data =[]
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
                    data.extend(data_get)
        except FileNotFoundError as err:
            print("\nPlease enter a valid file name with extension, or leave out --output to print to terminal")
            sys.exit(1)
        except KeyError as err:
            print(err)
            print("\n check arguments please")
            sys.exit(1)
    elif "num_pages" in inputs.keys():
        try: 
            for i in range(inputs['num_pages']):
                call = client.get("nc67-uf89",limit=inputs['page_size'],offset=inputs['page_size']*i)
                for record in call:
                    print(str(record))
                data.extend(call)
            print("No output file specified, outputting to terminal")

        except KeyError as err:
            print(err)
            print("\n check arguments please")  
            sys.exit(1)
      
    elif "page_size" in inputs.keys():
        
        while True:
            call=client.get("nc67-uf89",limit=10000)
            data.extend(call)
            if(len(call)<10000):
                break;
        
        for row in data:
            print(str(data))
        
        print(f"\n\nNumber of pages = {int(len(data)/inputs['page_size'])}")
        print(f"Number of rows = {len(data)}")
        print("No output file specified, outputting to terminal")
    else:
        print("Invalid arguments,'page_size' is required")
    
    return data
    

    
