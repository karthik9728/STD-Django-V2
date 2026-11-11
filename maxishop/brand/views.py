from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import View
from .models import Brand

# Create your views here.
# Class or Function Based View

# Function-Based View (FBV)
def brandFun(request):
    return HttpResponse("Brand Function")

# Class-Based View (CBV)
class BrandView(View):
    def get(self,request):
        return HttpResponse("Brand Class")

# def get(request):
#     brands = Brand.objects.all()
#     return render(request,"index.html",{'brands':brands})

# def details(request,id):
#     brand = get_object_or_404(Brand,id=id)
#     return render(request,"details.html",{'brand':brand})

def get(request,id = None):
    if(id is None):
        brands = Brand.objects.all()
        return render(request,"index.html",{'brands':brands})
    else:
        brand = get_object_or_404(Brand,id=id)
        return render(request,"details.html",{'brand':brand})
