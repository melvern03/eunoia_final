from django.shortcuts import render
from django.http import HttpResponse

import os
import json

from fatsecret import Fatsecret
from rest_framework.response import Response

consumer_key = '69d1000fa7d14010bb108c88c95d7442'
consumer_secret = 'fbfbb9e806f846b29ab53f7a13212076'

fs = Fatsecret(consumer_key, consumer_secret)

def home(request):
    return render(request,'web_front/home.html',{'title':'upload test'})

def fatsecret(request,makanan):
    try:
        foods=fs.foods_search(makanan)
        # foods = fs.foods_search("Ice Cream")
        food_result = fs.food_get(foods[0]['food_id'])
        food_json = json.dumps(food_result['servings']['serving'][0])
        return HttpResponse(food_json)
    except:
        return HttpResponse("error")

# def fatsecret_response(request,makanan):
#     try:
#         foods=fs.foods_search(makanan)
#         # foods = fs.foods_search("Ice Cream")
#         food_result = fs.food_get(foods[0]['food_id'])
#         food_json = json.dumps(food_result['servings']['serving'][0])
#         return Response(food_json)
#     except:
#         return Response("error")

# def fatsecret_without(request,makanan):
#     try:
#         foods=fs.foods_search(makanan)
#         # foods = fs.foods_search("Ice Cream")
#         food_result = fs.food_get(foods[0]['food_id'])
#         food_json = json.dumps(food_result['servings']['serving'][0])
#         return (food_json)
#     except:
#         return ("error")