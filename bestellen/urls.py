from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('broodjeshuis/', views.broodjeshuis, name='broodjeshuis'),
    path('walvis/', views.walvis, name='walvis'),
    path('broodjeshuis/bestellen/', views.broodjeshuis_bestellen, name='broodjeshuis_bestellen'),
    path('walvis/bestellen/', views.walvis_bestellen, name='walvis_bestellen'),
    path('broodjeshuis/bestellen/post/', views.broodjeshuis_bestellen_post, name='broodjeshuis_bestellen_post'),
    path('walvis/bestellen/post/', views.walvis_bestellen_post, name='walvis_bestellen_post'),
]