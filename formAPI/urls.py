from django.urls import path
from .views import AddDetials, DisplayDetials

urlpatterns = [
    path('add-details/',AddDetials.as_view(),name='add-details'),
    path('display-details/',DisplayDetials.as_view(),name='display-details'),
]
