import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#This identifies the html templates
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

#This acquires the json file, extracts the first value in Message, and sends it to the rendered HTML template to be displayed
def index(request):
    jsonFile = open('/home/nicholas/ACSG-515_Lab5/Lab5/home/hello-world.json')
    data = json.load(jsonFile)

    return render(request, "helloWorld.html", {"helloWorld": data[0]["Message"]})