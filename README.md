#**Project Title**

MyDiary

This is an online journal web application Diary where users can create and login to their account,add an entry to the his or her Diary.The user can view and edit the entries in the diary.The application sends notification to users prompting them to add an entry to their diary.  

#**Development**

This application was developed using python web framework,*Flask* and *Postgres* as the object-relational database system and *SQLAlchemy* as the Object Relation Mapper.The front end of the application was deleloped using *React JS*. 

#**Feautures**

Users are authenticated and validated JWT.Each user is unique and no account can be accessed by unauthenticated user.Users gets a recieves a prompt email to add an entry into their Diary.

#**Getting Started**
KIndly follow the below procedure to get a copy of this project up and running on your local machine:

###**Prerequisities**

Make sure your machine running python 3.6,Postman and the latest version of node js.

###**API Reference**

Please click on the following link to see API documentation.............

###**Running Tests**
   * Run:
     * $tests.py 

###**Installation**

- Make a directory of the project and initialize git.
- Clone the project repository from the following link
    $git clone............................................

####**1. Install API Dependencies** 

* Switch into Diary-API directory  create and activate a virtual enviroment as follows:
   * $cd Diary-API
   * $python3.6 -m venv virtual
   * $source virtual/bin/activate
* Install API dependencies as follows:
   * $sudo pip install -r requirements.txt

####**2. Create and Set up Postgres database .**

* Create database  
  * $createdb "mydiarydb"
* Run database migrations: 
  * $python manage.py db upgrade

After setting up the above,Run:

$ python run.py

####**3. Test end points using Postman**

####**4. Install Front-End-App modules. **

* Change directory to Front-End-App directory.
   * $cd Front-End-App

* Install React App modules:
   * $npm install

* Install the following Front-End-App dependencies
    * $npm install react-router-dom
    * $npm install axios
    * $npm install Navigation,Switch
    * $npm install --save react-redux

###**Languages**
     * API
       Created using Flask, a Python3.6 web Framework
     * Front-End
        Created using Javascript,Node JS and React JS.

###**Versioning**
      * Git is used for versioning.Click "here" to see the versions available.

###**Authors**

      * Antony - * Andela Project *

###**Acknowledgement**

        - Ann Mukundi *Project Instructor*

###**Licence**
    - This application is licenced under GNU licence