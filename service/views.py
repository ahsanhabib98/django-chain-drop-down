from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Service, SubCategory
from .forms import ServiceForm

class ServiceListView(ListView):
    model = Service
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('service_list')

def load_subcategory(request):
    category_id = request.GET.get('category')
    sub = SubCategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'service/dropdown_list_options.html', {'sub': sub})