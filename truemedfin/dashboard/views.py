from django.shortcuts import render, get_object_or_404
from .models import Item, List
from django.views.generic import ListView, DetailView
# Create your views here.

class ItemView(ListView):
    model = Item
    template_name = 'items.html'
    context_object_name = 'items'
  

class ListView(ListView):
    model = List
    template_name = 'lists.html'
    context_object_name = 'lists'



class ListDetailView(DetailView):
    model = List
    template_name = 'list_detail.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context
    
    def getListPrice(self, **kwargs):
        listPrice = sum(item.price for item in self.items)
        return listPrice
    

def list_detail_view(request, list_id):
        list_obj = get_object_or_404(List, id=list_id)
        return render(request, 'list_details.html', {'list': list_obj})
        
def dashboard(request):
    return render(request, 'dashboard.html')