# Create your views here.
from django.forms import ModelForm
from django.http import HttpResponse
from main.models import *
class TestForm(ModelForm):
        
    class Meta:
        model = TestModel


def home(request):
    
    form = TestForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        
    return HttpResponse("Created", status=200)