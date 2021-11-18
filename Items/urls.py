from django.urls import path

from . import views

urlpatterns = [
    path('grocery_list', views.index, name='index'),
    path('add_item/', views.add_item, name="add_item"),
    path('update/<int:item_id>', views.updateitem, name='updateitem'),
    path('delete/<int:item_id>', views.deleteitem, name='deleteitem'),


]