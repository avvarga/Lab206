from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
  context = {
  "date": strftime(" %d %b %Y ", gmtime()),
  "time": strftime(" %H:%M %p", gmtime())
  }
  return render(request,'time_display/index.html', context)
