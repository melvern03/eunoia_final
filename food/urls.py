from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='image_classification-home'),
    path('food/<makanan>',views.fatsecret,name='food'),
    path('foodv2/<makanan>',views.fatsecret_response,name='food-rest'),
    path('foodv3/<makanan>',views.fatsecret_without,name='food-plain')
]