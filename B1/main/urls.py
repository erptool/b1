from django.urls import path
from . import views


urlpatterns = [
     path('tip/', views.TipView, name='TipView'),
     path("", views.index, name="index"),
     path('search/', views.search_view, name='search_view'),
]
