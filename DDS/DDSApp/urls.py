from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.record_list, name='record_list'),
    path('create/', views.record_create, name='record_create'),
    path('handbook/', views.handbook_view, name='handbook'),
    path('edit/<int:pk>/', views.record_edit, name='record_edit'),
    path('delete/<int:pk>/', views.record_delete, name='record_delete'),
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('handbook/delete/<str:model_name>/<int:pk>/', views.delete_handbook_item, name='delete_handbook_item'),
    path('handbook/edit/<str:model_name>/<int:pk>/', views.edit_handbook_item, name='edit_handbook_item'),
]

