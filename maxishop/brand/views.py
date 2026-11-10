from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# Class or Function Based View

# Function-Based View (FBV)
def brandFun(request):
    return HttpResponse("Brand Function")

# Class-Based View (CBV)
class BrandView(View):
    def get(self,request):
        return HttpResponse("Brand Class")