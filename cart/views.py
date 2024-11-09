import telebot
from django.shortcuts import render,redirect
from django.views.generic import View
from main.models import Product
from django.contrib import messages
from .models import Cart,CartProducts,Order
from main.models import Category

bot = telebot.TeleBot("7412220605:AAEQD6X_F57VqQso2e8Kbd1yu1MHn06fW_M")
group_id = -1002028217344


def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    return cart


# Create your views here.
class CartView(View):
    
    def get(self, request):
        cart = cart_init(request)
        category = Category.objects.all()
        return render(request, "cart.html",{"cart":cart,'categories':category})

def add_product(request, product_id):
    cart = cart_init(request)
    cart.add(product_id)
    return redirect("/cart/")

def cart_product_update(request,action,product_id,item_id):
    cart = cart_init(request)
    item = CartProducts.objects.get(id=item_id)
    if item.quantity == 1 and action == "minus":
        return redirect("/cart/")
    else:
        cart.cart_product_update(action,product_id,item_id)
    return redirect("/cart/")


def deleteProduct(request,item_id):
    product = CartProducts.objects.get(id=item_id)
    cart = cart_init(request)
    cart.total_price -= product.price
    cart.total_quantity -= product.quantity
    cart.save()
    product.delete()
    print(product)
    return redirect('/cart/')    


def checkout(request):
    cart = cart_init(request)
    category = Category.objects.all()
    if request.method == "POST":
        user_cart = Cart.objects.get(id=int(request.POST.get("cart_id")))
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        street = request.POST.get("street")
        address = request.POST.get("address")
        if all([user_cart,phone,city,street,address]):
            Order.objects.create(cart=user_cart,phone=phone,city=city,street=street,address=address)
            text = f"""<b>Buyurtma bor !</b>\nTelefon : {phone}\nManzil : {city} {street} {address}\nTovar umumiy summa: {user_cart.total_price}"""
            bot.send_message(group_id,text,parse_mode="html")
            messages.success(request,"Sizning buyurtmangiz qabul qilindi !")
            return redirect("/cart/")
    return render(request, "checkout.html", {"cart":cart,'categories':category})