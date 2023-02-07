from django.urls import path
from . import views

urlpatterns = [

    path('', views.main_page, name='main_page'),
    path('wheat/create/', views.WheatCreate.as_view(), name='wheat-create'),
    path('wheat/open/today/', views.today_open, name='open-today'),
    path('wheat/open/week/', views.week_open, name='open-week'),
    path('wheat/open/month/', views.month_open, name='open-month'),
]