# Hidden Gems

This is a database project for the school I am attending, Code Institute. This project is for Milestone 3 (data-centric backend development). Its purpose is to prove that I can code backend Python logic.
 
## CHANGES
MongoDB database rename

logged into mongo cli

command:

show dbs



## UX
 
Basic website for showcasing data manipulation via CRUD in MongoDB. JQuery is used for the RWD hamburger side pop-out menu. MaterializeCSS is used for an increased overall appearance. MaterializeCSS was chosen over Bootstrap as I am not a fan of Bootstrap because it makes every website look identical and not custom, this is a personal preference of mine.

<br />
CRUD functions are handled via buttons for UI simplicity.

### User Stories/Extended Scenarios
    Anyone interested in locating Hidden Gems, which are local locations that don't get much if any publication, but are the most amazing places.

    The average user to this site could Register to become a Community Member and Login to access database features that are only available to registered users.

    Editing and Deleting posts directly communicates with MongoDB and only the post creator can see those buttons for their own posts.

    Everyone can view all posts.
******
### Wireframes, mockups, diagrams etc. that were created as part of the design process.
https://github.com/LogicAtom/TargetShooter/tree/main/wireframes/versions/version2

Documentation for wireframes: I have included the wireframes in sequential order to show my direction for the layout, even though the final product doesn't use some of the elements. Its pretty self explanatory.

#### Features
Feature 1  - MongoDB CRUD functionality
Feature 2  - User authorization
Feature 3  - RWD
 
## Testing
Result = Passed https://validator.w3.org/nu/?showsource=yes&doc=http%3A%2F%2Fflask-task-manager-project-koz.herokuapp.com%2F
<br />

Result = Errors(external libraries only) https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fflask-task-manager-project-koz.herokuapp.com%2F&profile=none&usermedium=all&warning=1&vextwarning=&lang=en

<br />
Performance Testing:
<br />
Result=Score 93
<br />
https://developers.google.com/speed/pagespeed/insights/?url=http%3A%2F%2Fflask-task-manager-project-koz.herokuapp.com%2F

<br />
I have performed extensive testing on each and every step of this project.
I had 3 other testers with different devices test as well. = Results, fully functional.

Compatibility Testing:

http://mobilehtml5.org/

Code Errors Testing:

DevTools > Toggle Device Toolbar

https://www.lambdatest.com/

https://jshint.com/

Validation Testing:

http://validator.w3.org/ (HTML5)
<br />
https://jigsaw.w3.org/css-validator/ (CSS3)

Performance Testing:

http://developers.google.com/speed/pagespeed/insights/

## Technologies Used

| Primary Languages | Template Engines & Frameworks |
| ------ | ------ |
| [HTML5](https://en.wikipedia.org/wiki/HTML5/ "HTML5") | [Jinja2](https://palletsprojects.com/p/jinja/ "Jinja2") |
| [Python3](https://www.python.org/ "Python3") | [Flask](https://flask.palletsprojects.com/en/2.0.x/ "Flask") |
| | [Django](https://www.djangoproject.com/ "Django") |

## API
PyMongo - https://docs.mongodb.com/drivers/pymongo/

## Database
MongoDB - https://www.mongodb.com/

| Servers | My Live Code |
| ------ | ------ |
| [GitHub](https://github.com/ "GitHub") | [Source Code](https://github.com/LogicAtom/flask-task-manager-project "Source Code") |
| [Heroku](https://www.heroku.com/platform "Heroku") | [My Live Site](http://flask-task-manager-project-koz.herokuapp.com "My Live Site") |

## Data Models
MongoDB Document Modeling<br />
Key: Value pairs<br /><br />
Collection Name: task_manager<br />
categories > category_name : value<br />
tasks > category_name:"Travel"<br />
example::<br />
task_name:"Snowshoe, WV"<br />
task_description:"Special event, snow tractor ride to candlelight dinner"<br />
is_urgent:"off"<br />
due_date:"01 February, 2005"<br />
created_by:"admin"<br />
users > username : value<br />
        password : value<br />

#### Assistant Services and Drivers
JQuery - https://jqueryui.com/
Materialize CSS - https://materializecss.com/
Amazon Web Services - https://aws.amazon.com/
[Git](https://git-scm.com/ "Git") : For Version Control System
[GitPod](https://gitpod.io/ "GitPod"): For Direct Interacting with Github

### Credits and Acknowledgements

Anthony Kozloski - Coder

Code Institute - FullStack Boot Camp - Most of the code and instructions was written by Code Institute, I cannot take credit for the code, only the customization of the code is actually mine.
<br />
Code Institute - for having me create a Python3 - Data Centric Development project

Code Institute - Tutors for all your help..you rock!
<br />
Code Institute - Student Care Team and Advisers..You are the most amazing people and I couldn't get this far without you!

### Educational Acknowledgements
Palmetto Goodwill - In collaboration with TTC - Grant Funder (my beautiful angels!)
<br />
Code Institute - Web Development School - You are the best Teachers!
<br />
Ed2Go/Cengage - Online Courses - You brought it all together, and offered the course. Awesome!


DevTools > Toggle Device Toolbar

https://www.lambdatest.com/

http://validator.w3.org/


http://developers.google.com/speed/pagespeed/insights/

https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal

https://ian.hixie.ch/ (The Editor of the HTML5 Spec)

I would personally like to thank my friends and family for putting up with me during the stress of building this project.

+ Audrey Kozloski: mom ...thanks for all those amazing home cooked meals!  yum :)
+ Rosie(hamster/ninja warrior): my 2am school break entertainer - She passed away September 2021, you will be missed my friend.

## 🚀 Features

You are just one command away to start your next project

- **Create Github Repo**

- **Create Organization Repo**

- **Open Project in IDE**

## 🦋 Prerequisite

- [Python](https://www.python.org/ "Python") Installed

- Python Basics Understanding

- [Git](https://git-scm.com/ "Git OFficial") Installed

- Git Basic Understanding

- [GH](https://cli.github.com/ "Github CLI") Installed

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

**🎇 You are Ready to Go!**

## Pip3 Installs
pip3 install dnspython
<br/>
pip3 install pymongo
<br />
pip3 install flask_pymongo
<br />
pip3 install Flask
<br />

## CLI
python3 <br />
python3 app.py (to start a development server)

## ❗ Available Commands

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

## 👷 Built with

- [Python](https://www.python.org/ "Python"): as Main Coding Language for executing commands

- [Batch](https://en.wikipedia.org/wiki/Batch_file "Batch") : For python file executor

- [Github](https://github.com/ "Github") : For Repo Storage and source code management

- [Git](https://git-scm.com/ "Git") : For Version Control System

- [Github CLI](https://cli.github.com/ "Github CLI"): For Direct Interacting with Github


## 🎊 Future Updates

- [x] Add project boilerplate automatically for different languages and frameworks

- [] Add GUI

- [x] Add Screenshots Folder

- [] Add Project to WorkSpaces

- [] Add Documentations

## 🧑🏻 Code Developer

**Anthony Kozloski**

- 🌌 [Profile](https://github.com/LogicAtom "Anthony Kozloski")

## Deployment/Environments

https://github.com/LogicAtom/flask-task-manager-project/deployments

Deployment via GitPod using git 
Alternate Deployment via Microsoft Visual Studio Code

CLONING:  https://github.com/LogicAtom/flask-task-manager-project.git (or) gh repo clone LogicAtom/flask-task-manager-project
via GitHub Desktop: x-github-client://openRepo/https://github.com/LogicAtom/flask-task-manager-project
Download .zip file:  https://github.com/LogicAtom/flask-task-manager-project/archive/refs/heads/main.zip