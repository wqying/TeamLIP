from django.urls import path 
from . import views 

urlpatterns = [ 
    path("", views.home, name="home"), 
    path("about/", views.about, name="about"), #about was swapped with home - for some reason this breaks when views.about and views.home are not switched
    path("savings/", views.savings, name="savings"),
    path("debt/", views.debt, name="debt"),
    #path("index/", views.index, name="index"),
    path("investing/", views.investing, name="investing"),
    path("map/", views.map, name="map"), #may need to edit to match
]