from django.urls import path
from .views import index, contact, getProductByID


urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('product/<int:id>', getProductByID, name='product')
]

