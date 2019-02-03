
from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import Item
from django.template import loader

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def item_list(request):
    template  = loader.get_template("index.html")
    return HttpResponse(template.render())