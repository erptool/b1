from django.urls import path
from . import views
from .views import detail_view, ObjectDetailView


urlpatterns = [
    path("", views.index, name="index"),
    path('tip/', views.TipView, name='TipView'),    
    path('search/', views.search_view, name='search_view'),
    path('detail/<int:pk>/', detail_view, name='detail_view'),
]
