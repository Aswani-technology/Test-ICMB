import json
from sqlite3 import connect

from colorama import Cursor
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import SalesTeam
from .forms import FormContactForm
from django.db import connection
from django.http import JsonResponse
from django.core import serializers



# Create your views here.
def home(request): #display home
    return render(request,'contactform.html')
@csrf_exempt
def sales_insert(request):#insert form data into table and redirect to grid view
    form= FormContactForm
    if request.method == 'POST':
        SalesTeam.firstname=request.POST.get('firstname')
        SalesTeam.lastname=request.POST.get('lastname')
        SalesTeam.email=request.POST.get('email')
        SalesTeam.phone=request.POST.get('phone')
        SalesTeam.company=request.POST.get('company')
        SalesTeam.hear_about_us=request.POST.get('hear_about_us')
        SalesTeam.comment=request.POST.get('comment')
        try:
            connect=connection.cursor()
            connect.execute("{call dbo.INSERTDATA(%s,%s,%s,%s,%s,%s,%s)}",(SalesTeam.firstname,SalesTeam.lastname,SalesTeam.email,int(SalesTeam.phone),SalesTeam.company,SalesTeam.hear_about_us,SalesTeam.comment))
            connect.commit()
        finally:
            connect.close()
    return redirect(request,sales_list)

def sales_list(request): #grid view to display all data
    try:
        connect=connection.cursor()
        connect.execute("GETDATA")
        result=connect.fetchall()
        
        connect.close()
        return render(request,'display.html',{'result':result})
        
    finally:
        
        connect.close()
def form_display(request): #ajax request to display data in modal
    id=request.GET.get('id')
    try:
        connect=connection.cursor()       
        user=connect.execute("{call dbo.SEARCH(%s)}", (id))
        connect.commit()
    
        data=json.dumps(list(user),default=str)
        print(user)
    finally:
        pass
        # connect.close()
    return JsonResponse(data,safe=False)

