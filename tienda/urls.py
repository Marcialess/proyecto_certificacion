
from django.urls import path
from .views import v_list

urlpatterns = [
    path('', v_list),
    
]