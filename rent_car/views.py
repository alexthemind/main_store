from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
from .models import CarBrand,CarModel,CarOrders,CarType
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.db import connection

# Create your views here.
def index(request):

    return render(request,'sections/index.html',{})

def login(request):

    return render(request,'sections/login.html',{})


def brands(request): 

    brandModel = CarBrand.objects.all().values()

    data = {
        'action': True,
        'data': list(brandModel)
    }

    return JsonResponse(data)


def models(request,brand):

    modelsBrand = CarModel.objects.filter(brand=brand).values()

    data = {
        'action': True,
        'data': list(modelsBrand)
    }

    return JsonResponse(data)


def types(request,model):

    typesModel = CarType.objects.filter(model=model).values()

    data = {
        'action': True,
        'data': list(typesModel)
    }

    return JsonResponse(data)


@csrf_protect
def setOrder(request):
    data = None

    if request.method == 'POST':


        brand = request.POST.get('brand')
        model = request.POST.get('model')
        type = request.POST.get('type')
        date_from = request.POST.get('from')
        date_to = request.POST.get('to')

        CarOrders.objects.create(brand=brand,model=model,type=type,date_from=date_from,date_to=date_to)

        data = {
            'action': True,
            'message': 'orden realizada!'
        }

    return JsonResponse(data)


def services(request):

    return render(request,'sections/services.html',{})


def orderList(request):

    return render(request,'sections/orders.html',{})


def getOrderList(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT ' + 
        'o.id' + 
        ',b.name AS brand' + 
        ',m.name AS model' + 
        ',t.type AS type' + 
        ',o.date_from' + 
        ',o.date_to ' +
        'FROM rent_car_carorders AS o ' + 
            'INNER JOIN rent_car_carbrand AS b ON o.brand = b.id ' + 
            'INNER JOIN rent_car_carmodel AS m ON o.model = m.id ' + 
            'INNER JOIN rent_car_cartype AS t ON o.type = t.id ' + 
        'WHERE o.status = 1')

        rows = dictfetchall(cursor)

    return JsonResponse({
        'data': rows
    }, safe=False)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]