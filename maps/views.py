from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
import json


# def index(request):
#     return HttpResponse("Hello, world. You're at the maps index.")

def index(request):

    mexico_city = {
        'lat': 19.432608,
        'lng': -99.133209
    }

    colombia = {
        'lat': 4.570868,
        'lng': -74.297333
    }
    
    list = [mexico_city, colombia]

    json_string1 = json.dumps(list)

    first_name = 'Rodrigo'
    last_name = 'Rubio'
    apiKey = ''
    template = loader.get_template('home.html')
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'apiKey': apiKey,
        'list':  json_string1
    }
    return HttpResponse(template.render(context, request))
