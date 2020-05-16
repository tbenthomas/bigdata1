import getopt,sys,os

def  get_inputs() -> dict:
 #instantiate dict that will be returned
 result={}
 
 #get terminal inputs
 try:
    options,remainder = getopt.getopt(sys.argv[1:],"p:n:o",['page_size=','num_pages=','output='])
 except getopt.GetoptError as err:
    print(str(err))

 #build dict that will be returned
 try:
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
            result['output'] = arg
 except UnboundLocalError as err:
     print("\nInvalid argument\nvalid arguments: --page_size,--num_pages,--output\n\n")
     sys.exit(1)

 #capture app key from enviroment
 try:
    result['APP_KEY']=os.environ['APP_KEY']
 except KeyError:
     print("\nPlease set your socrata api app token in an environment variable called APP_KEY")
     sys.exit(1)
 
 return result



