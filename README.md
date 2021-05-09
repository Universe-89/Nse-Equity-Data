# Nse-Equity-Data

This web app extracts data from the NSE website daily at 6 pm IST. Data extracted are code, open, high, low, close. This data is shown in a table.

## Setup
All the requirements are present in the ```requirements.txt```.To install into our machine run
```Python
pip install -r requirements.txt
```

## Deployed 

This website is Deployed on Heroku where Postgres is used as a database and Redis is used as cache [link](https://nse-data-info.herokuapp.com/)

## Overview

### All data about all equity are shown at first
![Home](https://github.com/tanmayks1999/Nse-Equity-Data/blob/main/Screenshots/home.png?raw=true)

### Search
Users can search for their desired equity and all the equity with a similar name will be shown to them. All queries are cached using Redis improving the performance of similar queries.

![Search](https://github.com/tanmayks1999/Nse-Equity-Data/blob/main/Screenshots/search.png?raw=true)

### Download
By clicking the download button all the information shown is downloaded in CSV format and the name of the file will be in formate (name searched) + (today's date).csv

![Search](https://github.com/tanmayks1999/Nse-Equity-Data/blob/main/Screenshots/download.png?raw=true)

### Data shown in cs

![Search](https://github.com/tanmayks1999/Nse-Equity-Data/blob/main/Screenshots/csv.png?raw=true)
