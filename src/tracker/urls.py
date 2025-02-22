from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search'),
    path('film/<int:pk>', views.film_detail, name='film-detail'),
]
