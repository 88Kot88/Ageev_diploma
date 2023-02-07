from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import TemplateView

from datetime import datetime

from django.db.models import Sum

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Wheat
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import PermissionRequiredMixin

def _is_foreman(user: User):
    return user.groups.filter(name='weigher_foreman').exists()

def _is_master(user: User):
    return user.groups.filter(name='elevator_master').exists()

def _is_director(user: User):
    return user.groups.filter(name='gen_director').exists()

@login_required
def main_page(request):
    query_set = Group.objects.filter(user=request.user)
    for g in query_set:
        query_set = g

    context = {
        'query_set': query_set
    }
    return render(request, 'main_page.html', context=context)

@user_passes_test(lambda user: any([_is_foreman(user), _is_master(user), _is_director(user)]))
@login_required
def today_open(request):
    today = Wheat.objects.filter(date=datetime.now())\
        .aggregate(Sum('weight'))

    for key, value in today.items():
        if value == None:
            today = 0
        else:
            today = format(value, '.2f')


    context = {
        'today': today,
        }
    return render(request, 'data/today_open.html', context=context)

@user_passes_test(lambda user: any([_is_master(user), _is_director(user)]))
@login_required
def week_open(request):
    day = datetime.now()
    weekk = day.strftime("%V")
    week = Wheat.objects.filter(date__week=weekk).aggregate(Sum('weight'))
    for key, value in week.items():
        if value == None:
            week = 0
        else:
            week = format(value, '.2f')

    context = {
        'week': week,
    }
    return render(request, 'data/week_open.html', context=context)

@user_passes_test(_is_director)
@login_required
def month_open(request):
    day = datetime.now()
    month = Wheat.objects.filter(date__year=day.year).aggregate(Sum('weight'))
    for key, value in month.items():
        if value == None:
            month = 0
        else:
            month = format(value, '.2f')

    context = {
        'month': month,
    }
    return render(request, 'data/month_open.html', context=context)

class WheatCreate(PermissionRequiredMixin, CreateView):

    permission_required = 'data.add_wheat'
    model = Wheat
    fields = ['weight']
    success_url = reverse_lazy('main_page')






