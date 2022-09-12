from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from .forms import theForm
from .models import pictureStore
import json
from base64 import b64encode

# Create your views here.
# the get request, gets a list of dog breeds
def dogs(request):
    # api for getting the dog breeds, can change the limit of breeds by changing the limit=
    url = 'https://api.thedogapi.com/v1/breeds?limit=10&page=0'

    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        dogs = response.json()
        # rendering the home page with the list of items
        return render(request, "home.html", {'dogs': dogs})
    else:
        print("Error:", response.status_code, response.text)

"""
# change name once i've build an api more suitable
# the post method and the page of the form being rendered
# basic dropbox api for testing if post works, basically just echos back whatever was in the query
def echoing(request):
    form = theForm()
    if request.method == "POST":
        # change once i have a better api for posting
        # basic dropbox api for testing if post works, basically just echos back whatever was in the query
        url = "https://api.dropboxapi.com/2/check/app"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRiYXJxMTlvcWdtaHhkOng3MXd5OHA2aTd1cjFsZA== '
            }
        payload = {}
        payload["query"]  = request.POST['words']
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == requests.codes.ok:
            print(response.text[11:-2])
            return HttpResponseRedirect('/')
        else:
            print("Error:", response.status_code, response.text)
            form = theForm()
    return render(request, 'form.html', {'form': form})
"""

# basic dropbox api for testing if post works, basically change the profile picture
def profilePic(request):
    if request.method == "POST":
        form = theForm(request.POST, request.FILES)
        f = request.FILES['picture'].file.getvalue()
        base64_bytes = b64encode(f)
        base64_string = base64_bytes.decode('utf-8')
        if form.is_valid():
            url = "https://api.dropboxapi.com/2/account/set_profile_photo"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer sl.BPHlRsQGUrgYhfxODrNcs1zuPxy2w266ttGknXROwIc3ZAac1sIC8Nlp3pQjY7UpzeVZvcPMLAEtMVY43xKpGxgbt5s_ax2_xOHeThwU5lEEBHZbMtY6CBL0i1SUYdhIz-Ohn3Vy1oY'
            }
            payload = {
                "photo": {
                    ".tag": "base64_data",
                    "base64_data": base64_string
                }
            }
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == requests.codes.ok:
                print(response.text[11:-2])
                return HttpResponseRedirect('/')
            else:
                print("Error:", response.status_code, response.text)
                print(json.dumps(payload))
                form = theForm()
            print('yes')
        else:
            print("invalid form")
            form = theForm()
    else:
        form = theForm()
    return render(request, 'form.html', {'form': form})