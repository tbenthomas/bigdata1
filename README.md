# bigdata1 

# About
This project seeks to create a terminal/shell interface aimed at pulling data from a dataset found in NYC Open Data.
Optionally, by utlizing docker-compose, a elasticsearch and kibana service will be started, allowing the creation of visuals and dashboards on Kibana.

The specific dataset that this project aims to work with is Open Parking and Camera Violations (OPCV) which we pull data from utilizing the socrata api.

# Part 1
This section will contain instructions on usage utilizing a docker container to run a command line interface to simply pull data from our data source. 

## Docker 
> A Docker container for a command line interface to simply pull data and either output to terminal or load into specified file is available at [Docker Container](https://hub.docker.com/r/tbenthomas/bigdata1) under tag 1.0. 

This docker container contains an image of an enviroment which will allow you to run the scripts without downloading extra
dependencies (e.g. sodapy package) and contains all required scripts (found in this repository).

## Command Line Arguments
### The main terminal argument that must be accompanied for this script are:
1. --page_size=

This is required because it specifies the amount of data the script will pull from the dataset.
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

# Part 2/3: ElasticSearch and Kibana
> All necessary files are included in this repository. This includes the necessary docker-compose.yml file as well as associated python scripts. 
### To use docker-compose run
> $ docker-compose up -d

This will start all the services outlined in docker-compose (python, elasticsearch, and Kibana). An elasticsearch service will be started on localhost:9200 and Kibana will be started on localhost:5201

### To run our python main script, load the data into elasticsearch, and subsequently make available to kibana, simply run

> docker-compose run -e APP_KEY={Your APP KEY} pyth python3 main.py --page_size={int} --num_pages={int}

Optionally you may specify an output file as before. 

### Kibana
#### After running the python script and loading the elastic search index, Kibana is able to interact with the loaded data.
#### Kibana will be running at port 5601 (localhost:5601). 
#### Using a sample of 10,000 violation records the following visuals were created:
##### Region map showing count of violations by state
![image](kibana_screenshots/map.png?raw=true)

Based on this map, as expected the majority of violations in our sample had license plates from New York State. There were violations from license plates in neighboring states as well and even some from the State of Florida. In a larger sample, it is expected that there will be records have license plates issued by other states as well.  
##### Stacked area chart showing violation counts by county, stacked by violation type. 

![image](kibana_screenshots/stacked_area?raw=true)

Based on this chart it can be see that the majority of violations in this sample were in the NYC county, with the majority of violations in each county with the exception of brooklyn being street cleaning. This is understandble because NYC has something called "Alternate Side Street Parking Rules" set up for street cleaning. Due to limiting parking and inconvenient timing of rules, many New Yorkers fall prey to violation across all five boroughs. 

In Brooklyn the highest number of violations in this sample were school zone violations. 
##### Pie chart showing Percentage of each violation amongst the sample of the date (10,000 records)

![image](kibana_screenshots/pie.png?raw=true)

This pie chart offers further evidence that the majority of violations are of type "NO PARKING-STREET CLEANING". Looking at the rest of the chart, it can be inferred that the majority of violations seem to be from parking violations. 

##### Heat Map colored by Average Fine amount for each issuing agency split up by license type. 

![image](kibana_screenshots/heatmap.png?raw=true)
