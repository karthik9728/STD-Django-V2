from django.urls import path
from .import views

urlpatterns = [
    path('function',views.brandFun),
    path('class',views.BrandView.as_view())
]
