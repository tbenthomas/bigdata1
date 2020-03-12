# bigdata1 

# About
This project seeks to create a terminal/shell interface aimed at pulling data from a dataset found in NYC Open Data.
Optionally, by utlizing docker-compose, a elasticsearch and kibana service will be started, allowing the creation of visuals and dashboards on Kibana.

The specific dataset that this project aims to work with is Open Parking and Camera Violations (OPCV) which we connect to using
a specific id that is hard encoded into the apicall.py script (under src).

# Usage
--------------------------------------------------------------------------------------------------------------------------
## Arguments
### The main terminal arguments that must be accompanied for this script are:
1. --page_size=

This is required because they specify the amount of data the script will pull from the dataset.
The dataset gets split into pages, so page size is required.

### Optional Parameters:
1. --output=
2. --num_pages=

If a proper output file is specified using this parameter, all data that is pulled by the script will be stored
in a output file under the name inputed for this parameter. 
If num_pages is not specified,pages will be calcualted based on specified page_size.

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

## Docker 
A docker container is available at [Docker Container](https://hub.docker.com/r/tbenthomas/bigdata1)

This docker container contains an image of an enviroment which will allow you to run the scripts without downloading extra
dependencies (e.g. sodapy package) and contains all required scripts (found in this repository).

You have a few options to run this from the docker container:

### Recommended Usage
1.
> $ docker run -t -e APP_KEY={Your APP KEY} -v $PWD:/app bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json

This should be run in a directory that contains this repository. The -v $PWD:/app will mount the current directory (local host)into the working directory of the docker container. After running you will see your output file in local host. 

2. 
Run your docker container to start an instance in interactive mode.
Then run the python3 script as specified above under header "Local Machine" above.

3.
> $ docker run -t -e APP_KEY={Your API KEY} bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 

You may have noticed that this does not contain the output parameter. This command will output the results of your script
to the terminal. 

### Other Usage
> $ docker run -t -e APP_KEY={YOUR API KEY} bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json

This is not recommended because it only runs an instance of your docker image and exits after;which is not ideal for working with output files.The reason being, the outputed file is created in the environemnt of that specific instance of the docker image. Since you are not in interactive mode, you will not be able to immediately interact with that file. 

# ElasticSearch and Kibana
## Optionally you can utilize the included docker-compose.yml file to use this terminal application
### Simply run this command
> $ docker-compose up -d

This will start all the services outlined in docker-compose (python, elasticsearch, and Kibana). An elasticsearch service will be started on localhost:9200 and Kibana will be started on localhost:5201

### To run our python main script, load the data into elasticsearch, and subsequently make available to kibana, simply run

> docker-compose run -e APP_KEY={Your APP KEY} pyth python3 main.py --page_size={int} --num_pages={int}

Optionally you may specify an output file as before. 

### Using Kibana
#### After running the python script and loading the elastic search index, Kibana is able to interact with the loaded data.
#### Kibana will be running at port 5601 (localhost:5601). 
#### Example visuals made using Kibana:
##### Region map showing count of violations by state
![image](kibana_screenshots/map_visual?raw=true)

##### Graph showing violation counts over time. Due to limits on number of buckets, the buckets were defaulted to represent months.

![image](kibana_screenshots/ticket_count_over_time.png?raw=true)

##### Pie chart showing Percentage of each violation amongst the sample of the date (5000 records)

![image](kibana_screenshots/pie_chart_violations.png?raw=true)

##### Heat Map colored by Average Fine amount for each issuing agency split up by license type. 

![image](kibana_screenshots/heatmap.png?raw=true)
