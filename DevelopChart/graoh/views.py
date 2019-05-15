from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum, Avg, Max, Min, Count
from .models import *


def index(request):
    datalist = Tbltmpcorrect.objects.all()
    mNop = Tbltmpcorrect.objects.values('mes_ing_ifal').filter(esta_oper_equi='NOP').annotate(dcount=Sum('monto_reque'))
    mOp = Tbltmpcorrect.objects.values('mes_ing_ifal').filter(esta_oper_equi='NOP').annotate(dcount=Sum('monto_reque'))
    mOpclmn = Tbltmpcorrect.objects.values('mes_ing_ifal').filter(esta_oper_equi='OPCLMN').annotate(dcount=Sum('monto_reque'))
    mOpclmy = Tbltmpcorrect.objects.values('mes_ing_ifal').filter(esta_oper_equi='OPCLMY').annotate(dcount=Sum('monto_reque'))
    promedio = Tbltmpcorrect.objects.values('mes_ing_ifal').annotate(dcount=Avg('monto_reque'))

    
    context ={
            'datalist':datalist,
            'mNop': mNop,
            'mOp': mOp,
            'mOpclmn': mOpclmn,
            'mOpclmy': mOpclmy,
            'promedio': promedio
    }

    return render(request,"graoh/index.html",context)
