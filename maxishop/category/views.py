from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Category
from .form import CategoryForm

# Create your views here.
def get(request,id = None):
    if(id is None):
        categories = Category.objects.all().order_by('name')
        return render(request,"category/index.html",{'categories':categories})
    else:
        category = get_object_or_404(Category,id=id)
        return render(request,"category/details.html",{'category':category})

def upsert(request,id=None):
    category = None
    if id:
         category = get_object_or_404(Category,id=id)
    if request.method == "POST" :
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()

            if id:
                messages.info(request, "Category updated successfully!")
            else:
                messages.success(request, "Category created successfully!")
                
            return redirect('category:list')           
    else:
        form = CategoryForm(instance=category)
        
    return render(request,"category/upsert.html",{'form':form})

def delete(request,id):
    category = get_object_or_404(Category,id=id)

    if request.method == "POST" :
        category.delete()
        messages.warning(request, "Category deleted successfully!")
        return redirect('category:list')

    return render(request, "category/delete.html", {'category': category})
    
