from django.conf.urls import url
from first_page import views

urlpatterns = [
    url('',views.index, name='index'),
]
