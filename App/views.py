from django.http import Http404
from django.shortcuts import render

from .models import NguoiDung

def index(request):
    context = {'menu': 'dashboard'}
    return render(request, 'App/index.html', context)

def detail(request, id):
    try:
        user = NguoiDung.objects.get(id=id)
    except NguoiDung.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'user': user, 'lichtrinh': user.lichtrinh.all().order_by('time_schedule')}
    return render(request, 'Detail/index.html', context)