# EatAtDCU #
#### Created by Shane Tully ####

EatAtDCU is a website displaying all the places to eat across all of Dublin City University’s (“DCU”) campuses. These include locations St. Patrick’s College, Glasnevin, All Hallows and DCU Alpha. Each location will display and give information on the cafe and restaurants available. This information may include opening times, weekend hours, and a location. Restaurants also feature an additional page showing what their daily special is. 

This website was built using Django, HTML, CSS, Javascript and JSON.

## Installation ##
1: Download the repository through the gitlab website or using "git clone https://gitlab.computing.dcu.ie/tullys7/2019-ca377-tullys7-EatAtDCU" in terminal with git installed.

2: Once the repository is downloaded go to the root folder, then go to "src/ca377" in terminal.

3: From here type "python manage.py runserver" or "python3 manage.py runserver" from the terminal. This will start the website.

4: Access the website from "http://127.0.0.1:8000/eatatdcu/"


## Deploy to Pythonanywhere ##
1: Create a pythonanywhere.com account.

2: Go to "2019-ca377-tullys7-EatAtDCU/src/ca377/ca377" directory and edit "settings.py" to include "YOUR_USERNAME.pythonanywhere.com" beside "ALLOWED_HOSTS".

3: Create a compressed file (zip, tar.gz) of the "src" and "data" file from the website root directory on your local machine.

4: On the "files" tab of your pythonanywhere.com account (top right) upload both of these compressed files.

5: Go to the Console tab (top right) and open a new bash console in another window.

6: Extract the two compressed files ("tar zxwf src.tag.gz").

7: In the bash terminal create a virtual environment to install Django. To do so type the following commands in the terminal in this order: "mkvirtualenv --python=/usr/bin/python3.5 eatatdcu-virtualenv", "pip install django=1.11", "pip install requests".

8: Go to the Web tab (top right) and click "Add new web app".

9: Select "manual configuration" and Python 3.5.

10: Set the source code and working directory values to "/home/YOUR_USERNAME/src/ca377".

11: Add the virtual environment "(eatatdcu-virtualenv) - "/home/YOUR_USERNAME/.virtualenvs/eatatdcu-virtualenv".

12: In the WSGI configuration file set the path to "/home/YOUR_USERNAME/src/ca377" and "os.environ['DJANGO_SETTING_MODULE']" to "ca377.settings".

13: Go back to the bash console with the virtual environment and type "./manage.py makemigrations", "./manage.py migrate", "./manage.py shell".

14: In the shell type "load_db_data".

15: Press the "reload" button on the Web tab.

16: Check if this worked at YOUR_USERNAME.pythonanywhere.com/eatatdcu.

17: (optional) to add static files go to the Web tab and under "Static Files" add the following value: "/static" - "/home/tullys7/src/ca377/eatatdcu/static".

## Run test cases ##
1: Go to "src/ca377" in the terminal.

2: Type "python3 manage.py test eatatdcu"

### Credits ###
Website created using Django documentations, w3schools for HTML and CSS, and various websites referenced in each file.