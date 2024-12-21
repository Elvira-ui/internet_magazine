from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse: 
    context: dict[str, Any]={
        'title':'Home',
        'content': 'Magazanin esas sehifesi - GULLER',
        'list': ['first', 'second'],
        'dict': {'first':1},
        'is_authenticated':True
         }
    return render (request, 'main/index.html',context)

def about(request) -> HttpResponse: 
    return HttpResponse ('About page')
