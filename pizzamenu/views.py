from django.shortcuts import render
from django.http import HttpResponse
import json
from .mock_data import MOCK_DATA
from django.views.decorators.csrf import csrf_exempt
from random import randint
# Create your views here.
def get_pizza(request, name):
    my_pizza = ''
    for pizza in MOCK_DATA:
        if pizza['name'] == name:
            my_pizza = pizza
            break
    
    return HttpResponse(json.dumps(my_pizza))

@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        ## Add Logic Later
        total_cost = 0
        for order in body:
            id = order['id']
            qty = order['quantity']
            price = 0
            for pizza in MOCK_DATA:
                if pizza['id'] == id:
                    price = qty*pizza['price']
            total_cost+=price
        order_id = randint(1, 10000)
        return HttpResponse(json.dumps({
            'order_id': order_id,
            'price': total_cost
        }))