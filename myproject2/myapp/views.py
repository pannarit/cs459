
from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import Item

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def item_list(request):
    html = ''' 
        <ul>
            <li>Banana</li>
            <li>Tea</li>
            <li>Milk</li>
        </ul> 
    '''

    for i in Item.objects.all():
        html = html +  '<li> %s %s %s %s </li>' %(i.name,i.description,i.price,i.expire)
    return HttpResponse(html)