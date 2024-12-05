from django.urls import path, include
from .views import ItemView, ListView, list_detail_view
urlpatterns = [
    path('items', ItemView.as_view(), name='items'),
    path('lists', ListView.as_view(), name='lists'),
    path('lists/<int:list_id>/', list_detail_view, name='list_detail'),
]
