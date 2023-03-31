from django.http import HttpResponse
from django.shortcuts import render
from .models import place,Team


# Create your views here.
def demo(request):
   obj=place.objects.all()
   team=Team.objects.all()
   return render(request,'index.html',{'result':obj,'result1':team})