from imp import IMP_HOOK
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Destination


def index(request):
    dests = Destination.objects.all()
    context = {
        'dests': dests
    }
    return render(request , 'travello/index.html', context)