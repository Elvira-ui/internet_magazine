from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse: 
    context: dict[str, Any]={
        'title':'Home - home page ',
        'content': 'Furniture Store HOME'
        
         }
    return render (request, 'main/index.html',context)

def about(request):
    context: dict[str, Any]={
        'title':'Home - about us',
        'content': 'About us',
        'text_on_page' : 'A text about why this store is so cool, and what a good product it is.'
        
         }
    return render (request, 'main/about.html',context)

   
