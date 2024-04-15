from django.urls import path
from . import views

urlpatterns = [
    path('watches/', views.WatchList.as_view(), name='watches'),
    path('watches/search/', views.WatchList.as_view(), name='watch-search'),
]
