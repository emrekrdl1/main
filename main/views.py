from django.shortcuts import render
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from django.http import *

def post_list(request):
    return render(request, 'post_list.html', {})