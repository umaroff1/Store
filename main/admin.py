from django.contrib import admin
from .models import Brand,Product,ProductImages,Rating,SubCategory,Category
# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',"stock","avilable","price",]
    list_display_links = ("name",)
    list_editable = ["price","stock","avilable" ]
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Rating)
admin.site.register(ProductImages)