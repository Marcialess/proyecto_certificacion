from django.shortcuts import render
from .models import Address,Salesorderheader
from django.contrib.auth.decorators import login_required


def valid_date(fecha_texto):
    from datetime import datetime
    try:
        return datetime.strptime(fecha_texto,"%Y-%m-%d")
    except:
        return False
@login_required
def v_list(request):
    consulta = Salesorderheader.objects.all()

    filter_code = request.GET.get('ordercode',False)
    if filter_code is not False:
        consulta = consulta.filter(salesorderid__startswith = filter_code)

    filter_city = request.GET.get('or-city',False)  
    if filter_city is not False:
        consulta = consulta.filter(shiptoaddressid__city__istartswith= filter_city)

    filter_zipcode = request.GET.get('zipcode',False)
    if filter_code is not False:
        consulta = consulta.filter(shiptoaddressid__postalcode__icontains= filter_zipcode)

    filter_date = valid_date(request.GET.get('shipdate',False))
    if filter_date is not False:
        consulta = consulta.filter(shipdate__gte = filter_date)


    p50 = consulta[:50]
    context = {
        'consulta':p50,
    }
    return render(request, 'list.html',context)

def v_login(request):
    pass


