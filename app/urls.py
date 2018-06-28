from django.conf.urls import url
from app import views


app_name = "app"

urlpatterns = [
    url(r'^register/$', views.register, name="register")
]
