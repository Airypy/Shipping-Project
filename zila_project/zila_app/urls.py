from django.urls import path
from zila_app import views

app_name='zila_app'

urlpatterns = [
    path('signin/',views.signin,name='signin')
]
