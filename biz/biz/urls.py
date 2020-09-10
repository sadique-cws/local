
from django.contrib import admin
from django.urls import path
from listing.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="homepage"),
    path('insert/',insert,name="insert"),
]
