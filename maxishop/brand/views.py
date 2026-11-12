from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Brand
from .form import BrandForm

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
        brands = Brand.objects.all().order_by('name')
        # brands = Brand.objects.all().order_by('-name')
        return render(request,"index.html",{'brands':brands})
    else:
        brand = get_object_or_404(Brand,id=id)
        return render(request,"details.html",{'brand':brand})

def create(request):
    form = BrandForm()
    if request.method == "POST" :
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand')
    else:
        form = BrandForm()
        
    return render(request,"create.html",{'form':form})

def edit(request,id):  
    brand = get_object_or_404(Brand,id=id)
    form = BrandForm()
    if request.method == "POST" :
        form = BrandForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand')
    else:
        form = BrandForm(instance=brand)
        
    return render(request,"edit.html",{'form':form})

def upsert(request,id=None):
    brand = None
    if id:
         brand = get_object_or_404(Brand,id=id)
    if request.method == "POST" :
        form = BrandForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand')
    else:
        form = BrandForm(instance=brand)
        
    return render(request,"upsert.html",{'form':form})

def delete(request,id):
    brand = get_object_or_404(Brand,id=id)

    if request.method == "POST" :
        brand.delete()
        return redirect('brand')

    return render(request, "delete.html", {'brand': brand})
    
