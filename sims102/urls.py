from django.urls import path
from . import views

app_name = 'sims102'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index_list'), 
    path('data/<int:pk>/', views.IndexDetailView.as_view(), name='index_detail'), 
    path('data/create/', views.IndexCreateView.as_view(), name='index_create'), 
]