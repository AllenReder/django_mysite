from django.shortcuts import render
from django.views import generic
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def search_form(request):
    return render(request, 'test_functions/search_form.html')

def search(request):
    if 'q' in request.GET:
        message = '你正在查找: %r' % request.GET['q']
    else:
        message = '你查找了个寂寞.'
    return HttpResponse(message)