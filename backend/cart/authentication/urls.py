from django.urls import path
from .views import CartList, AddressList
# from . import views

urlpatterns = [
    path('cart/', CartList.as_view(), name='cart-list'),
    path('address/', AddressList.as_view(), name='address-list'),
    # path('delete_cookie', views.delete_cookie, name='delete_cookie'),
]
