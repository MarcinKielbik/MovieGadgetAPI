from django.urls import path

from gadgets.views import gadget_list, gadget_detail

urlpatterns  = [
    path('gadgets/', gadget_list),
    path('gadgets/<int:pk>/', gadget_detail),
]