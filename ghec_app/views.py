from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
#from .graph import *





def home(request):
    return render(request, 'ghec/home.html')