from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Greeting
from .forms import FileForm

def parse_file(fPath):
    '''
    This is the main data parser. Data to be checked for type and format. Error trapping for alphanumeric and missing data.
    '''

    data = []
    for line in fPath.readlines():
        data.append([float(x.strip("\n")) for x in line.split(",")])
    return data

def index(request):

    data=[]
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            data = parse_file(request.FILES["newFile"])
        else:
            print file_form.errors
    else:
        file_form = FileForm()


    return render(request, 'index.html', {'form': file_form, 'data': json.dumps(data)})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

