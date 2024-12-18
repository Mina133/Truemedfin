from django.shortcuts import render, get_object_or_404
from .models import Item, List, WorkingHours, Depreciation, FixedOperationalCost, Specialization, total_operational_cost_per_hour
from django.views.generic import ListView, DetailView, TemplateView
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
        context['items'] = Item.objects.all()  # Add all items to the context
        return context
    
    def getListPrice(self, **kwargs):
        listPrice = sum(item.price for item in self.items)
        return listPrice
    
class AllItemsView(TemplateView):
    template_name = 'all_items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()  # Pass all items to the template
        return context
def list_detail_view(request, list_id):
        list_obj = get_object_or_404(List, id=list_id)
        return render(request, 'list_details.html', {'list': list_obj})
        
def dashboard(request):
    return render(request, 'dashboard.html')

class SpecializationView(TemplateView):
    template_name = "specialization.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch global parameters
        working_hours = WorkingHours.objects.first()
        fixed_cost = FixedOperationalCost.objects.first()
        depreciation = Depreciation.objects.first()

        # Handle missing data
        if not (working_hours and fixed_cost and depreciation):
            context["error"] = "Missing data for calculations."
            return context

        # Fetch specialization data
        specializations = Specialization.objects.all()
        specialization_data = [
            {
                "name": specialization.name,
                "cost_per_patient": specialization.cost_per_patient(working_hours, fixed_cost, depreciation),
                "service_cost": specialization.service_cost(working_hours, fixed_cost, depreciation),
            }
            for specialization in specializations
        ]

        # Add data to context
        context["hourly_rate"] = total_operational_cost_per_hour(working_hours, fixed_cost, depreciation)
        context["specializations"] = specialization_data

        return context