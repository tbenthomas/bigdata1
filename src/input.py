import getopt,sys,os

def  get_inputs() -> dict:
 options,remainder = getopt.getopt(sys.argv[1:],"p:n:o",['page_size=','num_pages=','output='])

 result={}
 for opt,arg in options:
     if opt=="--page_size":
         try:
             result['page_size']=int(arg)
         except:
             print("Error: Page_size must be an integer value")
     if opt=="--num_pages":
         try:
            result['num_pages'] =int(arg)
         except:
             print('Error: num_pages must be an integer value')
     if opt=="--output":
        if arg[-4:]=='json':
            result['output'] = arg

 result['APP_KEY']=os.environ['APP_KEY']
 
 return result



