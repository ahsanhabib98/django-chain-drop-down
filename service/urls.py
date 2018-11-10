from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('add/', views.ServiceCreateView.as_view(), name='service_add'),
    path('<int:pk>/', views.ServiceUpdateView.as_view(), name='service_change'),
    path('hr/ajax/load-sub/', views.load_subcategory, name='ajax_load_subcategory'),
]