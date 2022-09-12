# get-postAPI

to run the app:
first you need to have python 3, i used version 3.8.2
then install all the required libraries listed in requirement.txt, you can use "pip install -r requirement.txt"
then go into theAssignment folder
run "python manage.py makemigrations"
run "python manage.py migrate"
lastly run "python manage.py runserver" to run the server
go to http://127.0.0.1:8000/ for the demo

post method isn't going to work unless you have the appropriate access token, to use this specific api function
you will need an dropbox account and do everything required under "/set_profile_photo"

https://www.dropbox.com/developers/documentation/http/documentation#account-set_profile_photo

for people too lazy to read their documentation:
    you need to enable "account_info.write" in your account setting
    also make sure when you create the app in dropbox, give it full access, else account profile won't be covered
    then click the <get access token> in the example code