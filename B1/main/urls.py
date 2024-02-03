from django.urls import path
from . import views
from .views import ObjectDetailView


urlpatterns = [
    path("", views.index, name="index"),
    path('tip/', views.TipView, name='TipView'),    
    path('search/', views.search_view, name='search_view'),
    path('objects/<int:pk>/', ObjectDetailView.as_view(), name='object_detail'),
]
