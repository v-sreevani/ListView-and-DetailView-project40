from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView
class SchoolList(ListView):
    model=School
    template_name='school_list.html'
    context_object_name='SLO'
    ordering=['name']