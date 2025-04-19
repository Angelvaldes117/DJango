from django.urls import path

from .views import MyOrderView, CreateOrderProductView, DeleteMyOrderView

urlpatterns = [
    path('mi-orden', MyOrderView.as_view(), name="my_order"),
    path('agregar-producto', CreateOrderProductView.as_view(), name="add_product"),
    path('delete-my-order/', DeleteMyOrderView.as_view(), name='delete_my_order'),
]
