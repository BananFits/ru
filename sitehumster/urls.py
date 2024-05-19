from django.contrib import admin
from django.urls import path, include
from humster import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('humster.urls')),

]
admin.site.site_header = "Моя админка"
admin.site.index_title = "Сайт про путешествия"