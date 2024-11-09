from django.urls import path 
from . import  views

app_name = "main"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home" ),
    path("about/", views.About.as_view(), name="about" ),
    path('result', views.result_page , name = 'result'),
    path('category', views.category, name = 'category'),
    path("contact/", views.Contact.as_view(), name="contact" ),
    path("detail/<slug:slug>", views.product_detail, name="detail" ),
    path("wishlist/", views.WishListView.as_view(), name="wishlist" ),
    path("wishlist/add/<int:product_id>", views.add_wishlist, name="add_wishlist" ),
]
