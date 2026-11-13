from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Product
from .form import ProductForm

# Create your views here.
def get(request,id = None):
    if(id is None):
        products = Product.objects.all().order_by('name')
        return render(request,"product/index.html",{'products':products})
    else:
        product = get_object_or_404(Product,id=id)
        return render(request,"product/details.html",{'product':product})

def upsert(request,id=None):
    product = None
    if id:
         product = get_object_or_404(Product,id=id)
    if request.method == "POST" :
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()

            if id:
                messages.info(request, "Product updated successfully!")
            else:
                messages.success(request, "Product created successfully!")
                
            return redirect('product:list')           
    else:
        form = ProductForm(instance=product)
        
    return render(request,"product/upsert.html",{'form':form})

def delete(request,id):
    product = get_object_or_404(Product,id=id)

    if request.method == "POST" :
        product.delete()
        messages.warning(request, "Product deleted successfully!")
        return redirect('product:list')

    return render(request, "product/delete.html", {'product': product})
    
