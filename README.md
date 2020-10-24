# gigs 
## Author  
  
[virsail](https://github.com/virsail)  
  
# Description  
Python application built on Django framework that allows user to view upcoming events ,post an event and search for event ,a user also gets an email for confirmation after subscribing to event newsletter 
  
##  Live Link  
 Click [View Site]()  to visit the site
  
## Screenshots 
###### Home page
 ![Screenshot from 2020-10-23 22-58-01](https://user-images.githubusercontent.com/66640798/97077877-eea3a080-15ef-11eb-97e8-debb3db912f2.png)
 
 ###### Login page
 ![Screenshot from 2020-10-23 22-58-09](https://user-images.githubusercontent.com/66640798/97077906-30cce200-15f0-11eb-8029-71c94a59857b.png)

 ###### Home Page
 ![Screenshot from 2020-10-23 22-59-00](https://user-images.githubusercontent.com/66640798/97077940-94efa600-15f0-11eb-9bb5-c2aa544f12ad.png)

 
 ###### Search result
 ![Screenshot from 2020-10-23 22-59-14](https://user-images.githubusercontent.com/66640798/97077975-fadc2d80-15f0-11eb-91df-cd57c2a32d89.png)
## User Story  
 AS a user I would like to 
* Sign up and login to the application
* View all events that are yet to happen 
* Search for an event
* Post an event
* View different categories of events
* Get a confirmation email when i RSVP for an event
  

  
## Setup and Installation  
Clone the project folder  
  
##### Cloning the repository:  
 ```bash 
 git clone https://github.com/Virsail/gigs.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd gigs then pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Setup Database  
  SetUp your database User,Password, Host then make migration  
 ```bash 
python manage.py makemigrations eventsupdate 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 1.11.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* HTML
* CSS
* BOOTSTRAP
* AJAX
* JAVASCRIPT
  

## Contact Information   
ERICMBAGAYA@GMAIL.COM 
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Owiti-Charles/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2020 **VIRSAIL**
