from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # return render_to_response('index.html')
    
# this is a just a test line
def yo(request):
    return HttpResponse("This is the Yo Page") 

