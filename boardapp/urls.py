from django.urls import path
from .views import signupfunc, loginfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
]
