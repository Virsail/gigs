# gigs 
## Author  
  
[virsail](https://github.com/virsail)  
  
# Description  
Python application built on Django framework that allows user to view upcoming events ,post an event and search for event ,a user also gets an email for confirmation after subscribing to event newsletter 
  
##  Live Link  
 Click [View Site]()  to visit the site
  
## Screenshots 
###### Home page
 
 
 ###### Login page
 <img src="https://raw.githubusercontent.com/Owiti-Charles/Picture-Globe/master/static/images/searchfood.png"> 

 ###### Image Details 
 <img src="https://raw.githubusercontent.com/Owiti-Charles/Picture-Globe/master/static/images/modalscrn.png">
 
## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Owiti-Charles/Picture-Globe.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [mikeycharlesm7@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Owiti-Charles/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2019 **Owiti Charles**
