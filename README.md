# django-mangement-commands
Some additional django management commands to help you develop faster and effortlessly

## Prerequisite
Python 3.4+ (any version should work)
django 1.11+ (may also work on some lower versions)

## Installation
step 1: clone this project.

step 2: copy the management folder inside one of your apps in django (preferably your Root app).
Done :)

## Usage
After installing this you would have access to the following commands:

1) python manage.py createapp <new_app_name>
    This would create a brand new app with name <new_app_name> and **also add it to your setting.py INSTALLED_APPS list**.
    This would also create two directory hierarchy inside this app's folder namely:- 
    a) static/<new_app_name>/[css,css/fonts,js] .
    b) templates/<new_app_name>/ .
    
2) python manage.py destroyapp <app_name>
    This would delete the app from your project and remove it from the INSTALLED_APPS list inside setting.py file.
    
Note: Both of these commands will throw an exception if:
  a) The app already exists when creating.
  b) The app does not exists when deleting.
  c) You don't have enough previlage to read/write/create files/directories in the file system.
Both of these commands are tested in ubuntu 16 on pyhton 3.5 but should work on any platform.
Create an issues if it doesn't.

ENJOY :)
