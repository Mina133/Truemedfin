from django.urls import path, include
from .views import ItemView, ListView, list_detail_view, AllItemsView, SpecializationView
urlpatterns = [
    path('items', ItemView.as_view(), name='items'),
    path('lists', ListView.as_view(), name='lists'),
    path('lists/<int:list_id>/', list_detail_view, name='list_detail'),
    path('all-items/', AllItemsView.as_view(), name='all_items'),
    path('specializations/', SpecializationView.as_view(), name='specializations'),
]
