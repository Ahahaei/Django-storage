from django.shortcuts import render
from django.core.paginator import Paginator
from App.models import Product
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import FileResponse

# Create your views here.


def home (request):
    all_product=Product.objects.all().order_by('-created_at')
    paginator = Paginator(all_product, per_page=9)
    page_number = request.GET.get('page', 1)
    page_obj=paginator.get_page(page_number)
    return render(request,'home.html',{"products": page_obj.object_list,"paginator":paginator})
def add_product(request):
    if request.method == "POST":
        if request.POST.get('product')\
            and request.POST.get('purchase')\
            and request.POST.get('sale')\
            and request.POST.get('qty')\
            and request.POST.get('gender'):
            product= Product()
            product.product=request.POST.get('product')
            product.purchase=request.POST.get('purchase')
            product.sale=request.POST.get('sale')
            product.qty=request.POST.get('qty')
            product.gender=request.POST.get('gender')
            product.note=request.POST.get('note')
            product.save()
            return HttpResponseRedirect('/')
    else:
        return render (request, 'add.html')
def product(request, product_id):
    product=Product.objects.get(id=product_id)
    if product!=None:
        return render(request,'edit.html', {'product':product})
def edit_product(request,product_id):
    if request.method=="POST":
        product = Product.objects.get(id=product_id)
        if product != None:
            product.product=request.POST.get('product')
            product.purchase=request.POST.get('purchase')
            product.sale=request.POST.get('sale')
            product.qty=request.POST.get('qty')
            product.gender=request.POST.get('gender')
            product.note=request.POST.get('note')
            product.save()
            return HttpResponseRedirect('/')                                    
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('/')

def go_filter(request):
    return render(request, "go_filter.html")

def filter_product(request):
    qs=Product.objects.all()
    product_contains_query=request.GET.get('product_contains')
    sale_contains_query=request.GET.get('sale_contains')
    qty_contains_query=request.GET.get('qty_contains')
    min_contains_query=request.GET.get('min_purchase')
    max_contains_query=request.GET.get('max_purchase')
    qs=qs.filter(product=product_contains_query,sale=sale_contains_query,qty=qty_contains_query)
    context={
        'queryset':qs
    }
    return render(request, "filter_product.html", context)
def read_pdf(request):
    return render(request, "read_pdf.html")
from django.http import FileResponse

def serve_pdf(request):
    # Replace '/pdf/week.pdf' with the actual relative path to your PDF file
    pdf_file_path = '/static/pdf/week.pdf'
    # Open the PDF file in binary mode
    with open(pdf_file_path, 'rb') as pdf_file:
        response = FileResponse(pdf_file)
        return response
