from django.shortcuts import render

def index(request):
    context = {'menu': 'dashboard'}
    return render(request, 'App/index.html', context)