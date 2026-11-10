from django.urls import path
from .import views

urlpatterns = [
    path('',views.get),
    path('details/<int:id>/',views.details,name="details"),
    path('function',views.brandFun),
    path('class',views.BrandView.as_view())
]
