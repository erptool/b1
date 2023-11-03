from django.urls import path
from . import views
from .views import ObjectDetailView


urlpatterns = [
     path('tip/', views.TipView, name='TipView'),
     path("", views.index, name="index"),
     path('search/', views.search_view, name='search_view'),
     #path('objects/', ObjectListView.as_view(), name='object_list'),
    path('objects/<int:pk>/', ObjectDetailView.as_view(), name='object_detail'),
]
