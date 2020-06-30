from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from mpttapp.models import File
from mpttapp.forms import AddFileForm

# Create your views here.
def index(request):
    return render(request, "index.html", {'files': File.objects.all()})


def add_file_view(request):
    html = 'addfile.html'
    form = None
    if request.method == 'POST':
        form = AddFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
            )
            return HttpResponseRedirect(reverse,'homepage')

    form = AddFileForm()
    return render (request, html, {'form':form})




