from django.urls import path
from .import views

urlpatterns = [
    path('',views.get,name='brand'),
     # path('details/<int:id>/',views.details,name="details"),
    path('details/<int:id>/',views.get,name='details'),
    path('create',views.create),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('function',views.brandFun),
    path('class',views.BrandView.as_view())
]
