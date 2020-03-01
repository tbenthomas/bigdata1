# bigdata1 

# About
This project seeks to create a terminal/shell interface aimed at pulling data from a dataset found in NYC Open Data.

The specific dataset that this project aims to work with is Open Parking and Camera Violations (OPCV) which we connect to using
a specific id that is hard encoded into the apicall.py script (under src).

# Usage
--------------------------------------------------------------------------------------------------------------------------
## Arguments
### The main terminal arguments that must be accompanied for this script are:
1. --page_size=

This is required because they specify the amount of data the script will pull from the dataset.
The dataset gets split into pages, so page size is required.

### Optional Parameter:
1. --output=
2. --num_pages=

If a proper output file is specified using this parameter, all data that is pulled by the script will be stored
in a output file under the name inputed for this parameter. 
If num_pages is not specified pages will be calcualted based on specified page_size.

### Required Environment Variable
1. APP_KEY

Socrata API makes use of APP tokens in order to make api calls. As such, it is required that the environment that the 
main.py script is run on has a variable APP_KEY set to a proper APP_TOKEN. 

## How to run
### Local Machine
1. 
> $ python3 main.py --page_size=1000 --num_pages=4 
2. optional*
>$ python3 main.py --page_size=1000 --num_pages=4 --output={Your output file name}
3. optional**
>$ python3 main.py --page_size=1000 

It is required to run using python3 because function annotations are used. 

## Docker 
A docker container is available at [Docker Container](https://hub.docker.com/r/tbenthomas/bigdata1)

This docker container contains an image of an enviroment which will allow you to run the scripts without downloading extra
dependencies (e.g. sodapy package) and contains all required scripts (found in this repository).

You have a few options to run this from the docker container:

### Recommended Usage
1.
> $ docker run -t -e APP_KEY={Your APP KEY} -v $PWD:/app bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json
This should be run in a directory that contains this repository. The -v $PWD:/app will mount the current directory (local host)
into the working directory of the docker container. After running you will see your output file in local host. 

2. 
Run your docker container to start an instance in interactive mode.
Then run the python3 script as specified above under header "Local Machine"

3.
> $ docker run -t -e APP_KEY={Your API KEY} bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 
You may have noticed that this does not contain the output parameter. This command will output the results of your script
to the terminal. 

### Other Usage
> $ docker run -t -e APP_KEY='bsjUqp9lfHkP5xwfR4u3RNWWa'# bigdata1 

# About
This project seeks to create a terminal/shell interface aimed at pulling data from a dataset found in NYC Open Data.

The specific dataset that this project aims to work with is Open Parking and Camera Violations (OPCV) which we connect to using
a specific id that is hard encoded into the apicall.py script (under src).

# Usage
--------------------------------------------------------------------------------------------------------------------------
## Arguments
### The main terminal arguments that must be accompanied for this script are:
1. --page_size=
2. --num_pages=

These are required because they specify the amount of data the script will pull from the dataset. 

### Optional Parameter:
1. --output=

If a proper output file is specified using this parameter, all data that is pulled by the script will be stored
in a output file under the name inputed for this parameter. 

### Required Environment Variable
1. APP_KEY

Socrata API makes use of APP tokens in order to make api calls. As such, it is required that the environment that the 
main.py script is run on has a variable APP_KEY set to a proper APP_TOKEN. 

## How to run
### Local Machine
1. 
> $ python3 main.py --page_size=1000 --num_pages=4 
2. optional*
>$ python3 main.py --page_size=1000 --num_pages=4 --output ={Your output file name}
It is required to run using python3 because function annotations are used. 

## Docker 
A docker container is available at [Docker Container](https://hub.docker.com/r/tbenthomas/bigdata1)

This docker container contains an image of an enviroment which will allow you to run the scripts without downloading extra
dependencies (e.g. sodapy package) and contains all required scripts (found in this repository).

You have a few options to run this from the docker container:

### Recommended Usage
1.
> $ docker run -t -e APP_KEY={Your APP KEY} -v $PWD:/app bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json
This should be run in a directory that contains this repository. The -v $PWD:/app will mount the current directory (local host)
into the working directory of the docker container. After running you will see your output file in local host. 

2. 
Run your docker container to start an instance in interactive mode.
Then run the python3 script as specified above under header "Local Machine"

3.
> $ docker run -t -e APP_KEY={Your API KEY} bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 
You may have noticed that this does not contain the output parameter. This command will output the results of your script
to the terminal. 

### Other Usage
> $ docker run -t -e APP_KEY={YOUR API KEY} bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json
This is not recommended because it only runs an instance of your docker image and exits after;which is not ideal for working with output files.

The reason being, the outputed file is created in the environemnt of that specific instance of the docker image. 
Since you are not in interactive mode, you will not be able to immediately interact with that file.  bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json
This is not recommended because it only runs an instance of your docker image and exits after;which is not ideal for working with output files.

The reason being, the outputed file is created in the environemnt of that specific instance of the docker image. 
Since you are not in interactive mode, you will not be able to immediately interact with that file. 
