from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .forms import FileForm

# Create your views here.
def index(request):

    file_upload = []
    string = ''
    if request.method == 'POST':
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            print('valid')
            for line in request.FILES["newFile"].readlines():
                print(line)
        else:
            print file_form.errors
    else:
        file_form = FileForm()

    return render(request, 'index.html', {'form': file_form, 'data': string})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

