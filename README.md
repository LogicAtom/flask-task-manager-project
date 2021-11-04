# Task Manager

About: This is a database project for the school I am attending, Code Institute. This project is for Milestone 3 (data-centric backend development). 

Purpose: To provide a database that is intuitive to use and easy to interact with while looking good and being mobile web responsive.
 
## 🚀 Features

- [x] MongoDB CRUD functionality

- [x] CSS enhanced GUI

- [x] Security

- [x] Mobile Responsive web design with JQuery hamburger menu

- [x] Add Documentation

### 🎊  Security Features
Environment variable <br />
.gitignore <br />
User Authentication <br />

## MAJOR CHANGES
Redesigning project into a general usage Task Manager

file names changes:

get_gems to get_tasks

gems to tasks

gem to task

JQuery Form Validation (custom error messages)

npm install jquery

### CHANGES
MongoDB database rename

logged into mongo cli

command:

show dbs

help

use task_manager

<br />
'''''
<code>db.getCollectionNames().forEach(function(collName) {
    db[collName].find().forEach(function(d){
        db.getSiblingDB('ms3_db')[collName].insert(d); 
    }) 
});
</code><br />
=== SUCCESS ...copied Database named: task_manager, to, a new Database, named: ms3_db
<br />
Database help answers:<br />
https://stackoverflow.com/questions/9201832/how-do-you-rename-a-mongodb-database/57811701#57811701
https://stackoverflow.com/a/48372759/13254826
''''
<br />

Now I need to rename the 'tasks' collection to 'gems'...
<br />
<code>use ms3_db</code> to switch to that database., then type this to rename the collection<br />
<code>db.tasks.renameCollection('tasks')</code><br />
https://stackoverflow.com/a/8732666/13254826
<br />

********* ATTEMPT 1....SUCCESS!

show collections

now shows:
1. categories
2. gems
3. users

## UX
 
Basic website for showcasing data manipulation via CRUD in MongoDB. JQuery is used for the RWD hamburger side pop-out menu. MaterializeCSS is used for an increased overall appearance.

<br />
CRUD functions are handled via buttons for UI simplicity.

### User Stories/Extended Scenarios
    Average person looking to add Tasks into a MongoDB database with a calendar due date and urgent or non-urgent switch.

    Editing and Deleting posts directly communicates with MongoDB and only the post creator can see those buttons for their own posts.

    Everyone can view all posts.
******
### Wireframes, mockups, diagrams etc. that were created as part of the design process. 
PLEASE NOTE THAT THIS SECTION NEEDS UPDATING

https://github.com/LogicAtom/TargetShooter/tree/main/wireframes/versions/version2

Documentation for wireframes: I have included the wireframes in sequential order to show my direction for the layout, even though the final product doesn't use some of the elements. Its pretty self explanatory.


## 🛠️ Installation Steps

1. Clone the repository

```Bash
git clone https://github.com/LogicAtom/flask-task-manager-project.git
```

2. Change the working directory

```Bash
cd flask-task-manager-project.htm
```

3. Add Environment Variable path of this directory

4. Run the app using terminal

The dependancies should automatically install via the "requirements.txt" file, but just in case I have included the methods for manually installing the dependancies written directly below as pip3:

## Pip3 Installs
pip3 install dnspython
<br/>
pip3 install pymongo
<br />
pip3 install flask_pymongo
<br />
pip3 install Flask
<br />

## Deployment/Environments

https://github.com/LogicAtom/flask-task-manager-project/deployments

Deployment via GitPod using git 
Alternate Deployment via Microsoft Visual Studio Code

CLONING:  https://github.com/LogicAtom/flask-task-manager-project.git (or) gh repo clone LogicAtom/flask-task-manager-project
via GitHub Desktop: x-github-client://openRepo/https://github.com/LogicAtom/flask-task-manager-project
Download .zip file:  https://github.com/LogicAtom/flask-task-manager-project/archive/refs/heads/main.zip

### Terminal Shell commands
python3 <br />
python3 app.py (to start a development server)

### 🦋 Prerequisite

- [Python](https://www.python.org/ "Python3") Installed

- Python Basics Understanding

- [Git](https://git-scm.com/ "Git OFficial") Installed

- Git Basic Understanding

- [MongoDB](https://www.mongodb.com/ "MongoDB Atlas") Installed

**🎇 You are Ready to Go!**

### ❗ Available Commands

In the project directory, you can run:

```Bash
create
```

Either run this command in the project folder or set the path of `create.bat` in the environmental variable for executing create command anywhere (Run, cmd, or PowerShell).

```Bash
create <project_name>
```

For creating Local Repo use this command and it will create a local repository in the path provided.

```Bash
create <project_name> -g
```

For creating a Global Repo use this command and it will create a global repository on your GitHub profile using `gh` and make & push the initial commit.

```Bash
create <project_name> -o
```

For creating an Organization Repo use this command and it will create an Organization repository on your GitHub profile using `gh` and make & push the initial commit

> If you pass any other option like `-pr` then the repo will be private otherwise it will be public

## TESTING

### Compatibility Testing:

http://mobilehtml5.org/

### Code Testing
MongoDB Code Testing:
https://mongoplayground.net/

Python Code Testing:
https://pythontutor.com/

Result = Passed https://validator.w3.org/nu/?showsource=yes&doc=http%3A%2F%2Fflask-task-manager-project-koz.herokuapp.com%2F

Result = Errors(external libraries only) https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fflask-task-manager-project-koz.herokuapp.com%2F&profile=none&usermedium=all&warning=1&vextwarning=&lang=en

### Code Errors Testing:

DevTools > Toggle Device Toolbar

https://www.lambdatest.com/

https://jshint.com/

### Problems during Development
GitPod latency crash > my quick fix = change networks, and make Repo Private

### Validation Testing:

http://validator.w3.org/ (HTML5)

https://jigsaw.w3.org/css-validator/ (CSS3)

### Performance Testing:

Result=Score 93

https://developers.google.com/speed/pagespeed/insights/?url=http%3A%2F%2Fflask-task-manager-project-koz.herokuapp.com%2F

## 👷 Built with these Technologies

| Primary Languages | Template Engines & Frameworks |
| ------ | ------ |
| [HTML5](https://en.wikipedia.org/wiki/HTML5/ "HTML5") | [Jinja2](https://palletsprojects.com/p/jinja/ "Jinja2") |
| [Python3](https://www.python.org/ "Python3") | [Flask](https://flask.palletsprojects.com/en/2.0.x/ "Flask") |
| | [Django](https://www.djangoproject.com/ "Django") | 
| | [CSS3](https://materializecss.com/ "MaterializeCSS") |

### APIs
PyMongo - https://docs.mongodb.com/drivers/pymongo/

### Database
MongoDB - https://www.mongodb.com/

| Servers | My Live Code |
| ------ | ------ |
| [GitHub](https://github.com/ "GitHub") | [Source Code](https://github.com/LogicAtom/flask-task-manager-project "Source Code") |
| [Heroku](https://www.heroku.com/platform "Heroku") | [My Live Site](http://flask-task-manager-project-koz.herokuapp.com "My Live Site") |

## Data Models
MongoDB Document Modeling<br />
Key : Value pairs<br /><br />
Collection Name : task_manager<br />
categories > category_name : value<br />
tasks > category_name : "Travel"<br />
task_name:"Snowshoe, WV"<br />
task_description : "Special event, snow tractor ride to candlelight dinner"<br />
is_urgent : "off"<br />
due_date : "01 February, 2005"<br />
created_by : "user"<br />
users > username : value<br />
        password : value<br />

#### Assistant Services and Drivers
NodeJS - https://nodejs.org/en/download/ = Dependency Manager<br />
JQuery - https://jqueryui.com/ = Hamburger Mobile Side Menu<br />
Materialize CSS - https://materializecss.com/ = Enhance UI/UX<br />
Amazon Web Services - https://aws.amazon.com/ = Database Connector <br />
[Git](https://git-scm.com/ "Git") : Version Control System <br />
[GitPod](https://gitpod.io/ "GitPod") : IDE <br />
FontAwesome.com = Custom Icons

### Credits and Acknowledgements

## 🧑🏻 Code Developer

**Anthony Kozloski**

- 🌌 [Profile](https://github.com/LogicAtom "Anthony Kozloski")

Code Institute - FullStack Boot Camp - Most of the code and instructions was written by Code Institute, I cannot take credit for the code, only the customization of the code is actually mine.
<br />
Code Institute - for having me create a Python3 - Data Centric Development project

Code Institute - Tutors for all your help..you rock!
<br />
Code Institute - Student Care Team and Advisers..You are the most amazing people and I couldn't get this far without you!

stackoverflow - For all of the custom questions and answers.

### Educational Acknowledgements
Palmetto Goodwill - In collaboration with TTC - Grant Funder (my beautiful angels!)
<br />
Code Institute - Web Development School - You are the best Teachers!
<br />
Ed2Go/Cengage - Online Courses - You brought it all together, and offered the course. Awesome!
<br />
Charleston County Public Library - Thank you for letting me borrow around 100 books!

### Personal Acknowledgements
+ Audrey Kozloski: mom ...thanks for all those amazing home cooked meals!  yum :)
+ Rosie(hamster/ninja warrior): my 2am school break entertainer - She passed away September 2021, you will be missed my friend.
