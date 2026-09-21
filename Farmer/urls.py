from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('news',views.news,name='news'),
    path('market',views.market,name='market'),
    path('crops',views.crops,name='crops'),
    path('government',views.government,name='government'),
    path('expert',views.expert,name='expert'),
    path('trainning',views.trainning,name='trainning'),
    path('home',views.home,name='home'),

]