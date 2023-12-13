from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('cars/all/', views.AllCarsListView.as_view(), name='all-cars-list'),  
    path('cars/delete/<int:pk>/', views.CarDeleteView.as_view(), name='car-delete'), 
    path('cars/update/<int:pk>/', views.CarUpdateView.as_view(), name='car-update'), 
]