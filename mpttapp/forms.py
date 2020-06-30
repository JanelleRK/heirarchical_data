from django import forms
from mpttapp.models import File
from mptt.forms import TreeNodeChoiceField



class AddFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    category = TreeNodeChoiceField(queryset=File.objects.all())