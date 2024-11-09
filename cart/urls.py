from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.CartView.as_view(), name="cart"),
    path("add/<int:product_id>", views.add_product, name="add_to_cart"),
    path("cart_product_update/<str:action>/<int:product_id>/<int:item_id>", views.cart_product_update, name="cart_product_update"),
    path('cart/<int:item_id>',views.deleteProduct,name='delete'),
    path("checkout/", views.checkout, name="checkout"),
    ]