# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from firstapp.models import Topic,Webpage,AccessRecord
# from django.http import HttpResponse

# Create your views here.

def index(request):
    
    # my_dict = {'mensagem': "Hello World from first App!"}
    lista_paginas = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": lista_paginas}
    return render(request, 'firstapp/index.html', context=date_dict)
