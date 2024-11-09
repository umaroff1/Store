from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from .models import Product,Category,Rating
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import RatingForm
# Create your views here.



class HomePageView(ListView):
    queryset  = Product.objects.all().order_by('?')
    template_name = "index.html"
    context_object_name = 'item'
    def get_queryset(self):
        return Product.objects.filter(avilable=True).filter(subcategory__category__slug="smartfonlar")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Product.objects.filter(subcategory__category__slug="chexollar") 
        context["headphones"] = Product.objects.filter(subcategory__category__slug__in=["quloqchinlar", "simsiz-quloqchinlar",'smart-soatlar']) 
        context["categories"] = Category.objects.all() 
        print(context["cases"])
        return context
    



def product_detail(request, slug):

    product = Product.objects.get(slug=slug)

    ratings = Rating.objects.filter(product=product)
    category = Category.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('user')
        comment = request.POST.get('body')

        if name and comment:
            Rating.objects.create(name=name, comment=comment, product=product)
            print(name,comment,product)
        else:
            pass
        return redirect('main:detail', slug=slug)

    context = {
        'object': product,  
        'ratings': ratings,
        'categories':category
    }
    return render(request, 'detail.html', context)



class About(ListView):
    model = Category
    template_name = "about.html"
    context_object_name = "categories"




class Contact(ListView):
    model = Category
    template_name = "contact.html"
    context_object_name = "categories"





def result_page(request):
    q = request.GET.get('query')
    category = Category.objects.all()
    if len(q)>=2:
        query1 = Product.objects.filter(name__icontains = q)
    else:
        pass

    return render(request,'result.html',{'query':query1,'categories':category})


def category(request):
    c = request.GET.get('category')
    cat = Product.objects.filter(subcategory__category__name=c)
    category1 = Category.objects.all()
    print(c)
    print(cat)
    return render(request,'category.html',{'objects':cat,'categories':category1})



class WishListView(ListView):
    model = Product
    template_name = "liked_product.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    def get_queryset(self):
        try:
            wishlist = self.request.session["wishlist"]
        except:
            wishlist = self.request.session["wishlist"] = []
        return Product.objects.filter(id__in=wishlist)

def add_wishlist(request,product_id):
    product = Product.objects.get(id=product_id)
    request.session.modified = True
    try:
        wishlist = request.session["wishlist"]
    except:
        wishlist = request.session["wishlist"] = []
    if product.id in wishlist:
        wishlist.remove(product.id)
        messages.info(request,"Tovar wishlistdan o'chirildi !")
    else:
        wishlist.append(product.id)
        messages.info(request,"Tovar wishlistga qo'shildi !")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))