from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mpttapp.models import File
from mpttapp.forms import AddFileForm

# Create your views here.
def index(request):
    return render(request, "index.html", {'files': File.objects.all()})


def add_file_view(request):
    html = 'addfile.html'
    if request.method == 'POST':
        form = AddFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
                parent=data['parent']
            )
            return HttpResponseRedirect(reverse, 'homepage')

    form = AddFileForm()
    return render (request, html, {'form':form})




