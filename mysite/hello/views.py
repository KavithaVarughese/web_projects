from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.

def index(request):

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    ctx = {'num_visits' : num_visits}
    response = render(request, 'hello/index.html', ctx)
    response.set_cookie('dj4e_cookie', 'c4414e53', max_age=1000)

    return response