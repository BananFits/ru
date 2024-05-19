from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='home'),
    path('addpost/', addpost, name='addpost'),
    path('cats/<int:cat_id>/', category),
    path('cats/<slug:cat_slug>/', category_slug),
    path('travelid/<int:id>/', show_travelid, name='travelid'),
    path('travelsid/', travelsid, name='travelsid'),
    path('travelslug/<slug:sl>/', show_travelsl, name='travelslug'),
    path('travels-slug/', travelslug, name='travels-slug'),
]
