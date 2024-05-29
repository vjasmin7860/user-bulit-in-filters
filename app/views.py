from django.shortcuts import render
import datetime

# Create your views here.
def filters(request):
    da=datetime.datetime.now()
    d={'data':'hi hOW Are YOu JaSmiN','da':da,'c':2}
    return render(request,'filters.html',d)


def userfilters(request):
    d={'data':'Hi PYthOn HoW ARE yOu'}
    return render(request,'userfilters.html',d)