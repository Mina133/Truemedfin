from django.urls import path, include
from .views import ItemView, ListView
urlpatterns = [
    path('items', ItemView.as_view(), name='items'),
    path('lists', ListView.as_view(), name='lists'),
]
