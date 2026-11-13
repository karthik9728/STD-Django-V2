from django.shortcuts import render
from product.models import Product
from brand.models import Brand
from category.models import Category

def home(request):

    products = Product.objects.select_related('brand','category').all().order_by('-created_on')

    brands = Brand.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')

    # Search by product name
    search = request.GET.get('search','').strip()

    if search:
        products = products.filter(name__icontains=search)

    # Filter by brand
    brand_id = request.GET.get('brand')

    if brand_id:
        products = products.filter(brand_id=brand_id)

     # Filter by category
    category_id = request.GET.get('category')

    if category_id:
        products = products.filter(category_id=category_id)

    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
        'search': search,
        'selected_brand': brand_id,
        'selected_category': category_id,
    }

    return render(request, "home.html",context)