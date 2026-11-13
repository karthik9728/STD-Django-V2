from django.urls import path
from .import views

app_name = 'product'

urlpatterns = [
    path('',views.get,name='list'),
    path('details/<int:id>/',views.get,name='details'),
    path('create',views.upsert,name="create"),
    path('edit/<int:id>/',views.upsert,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
]
