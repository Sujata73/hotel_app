from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.db import connection
from .forms import RoomForm,RoombookingsForm,PaymentsForm
from datetime import date
from .models import Rooms, Roombookings, Payments
# Create your views here.


def index(request):
    return render(request,"files/index.html")


def rooms(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            # roomnumber = room_form.cleaned_data['Room Number']
            # roomprice = room_form.cleaned_data['Room Price']
            # roomtype = room_form.cleaned_data['Room Type']
            # roomcapacity = room_form.cleaned_data['Room Capacity']
            form.save()
            return redirect('/rooms_added/')
    return render(request,'files/rooms.html',{'form': RoomForm()})

def rooms_added(request):

    return HttpResponse("Rooms Added Successfully")

def bookings(request):
    if request.method == 'POST':
        form = RoombookingsForm(request.POST)
        if form.is_valid():
            # roomnumber = room_form.cleaned_data['Room Number']
            # roomprice = room_form.cleaned_data['Room Price']
            # roomtype = room_form.cleaned_data['Room Type']
            # roomcapacity = room_form.cleaned_data['Room Capacity']
            form.save()
            return redirect('/bookings_added/')
    return render(request,'files/bookings.html',{'form': RoombookingsForm()})

def bookings_added(request):

    return HttpResponse("Bookings Added Successfully")

def payments(request):
    if request.method == 'POST':
        form = PaymentsForm(request.POST)
        if form.is_valid():
            # roomnumber = room_form.cleaned_data['Room Number']
            # roomprice = room_form.cleaned_data['Room Price']
            # roomtype = room_form.cleaned_data['Room Type']
            # roomcapacity = room_form.cleaned_data['Room Capacity']
            form.save()
            b_id = form.cleaned_data['bookingid']
            return redirect('/invoice/'+str(b_id))
    return render(request,'files/payments.html',{'form': PaymentsForm()})

def payments_added(request):

    return HttpResponse("Payments Done Successfully")

def api(request,id):
    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    with connection.cursor() as cursor:
        cursor.execute('select bookingfrom,bookingto,roomprice from roombookings inner join rooms on assignroomid = roomid where bookingid = %s',[id])
        r = dictfetchall(cursor)
    price_list = []
    for i in r:
        d0 = i['bookingfrom']
        d1 = i['bookingto']
        delta = d1-d0
        price = i['roomprice'] * delta.days
        price_list.append(price)

    context = {}
    for i in price_list:
        context['total_price'] = i
    return JsonResponse(context)


def invoice(request,id):
    obj_1 = Roombookings.objects.filter(customername__icontains=id)
    obj_2 = Payments.objects.filter(bookingid__customername__icontains=id)
    context = {'obj_1':obj_1,'obj_2': obj_2}
    return render(request,"files/invoice.html",context)
