from django.conf.urls import url

from userinfo import views


urlpatterns = [
    url(r'register', views.register)
]