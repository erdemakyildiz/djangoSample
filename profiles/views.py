# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.

def list(request):
    return render(request, "profile/list.html")