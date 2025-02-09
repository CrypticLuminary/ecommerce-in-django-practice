from django.contrib import admin
from .models import category,product
from django.utils.html import format_html

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','category_description']
    search_fields = ['category_name','category_description']
    list_filter = ['category_name','category_description']


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_price','Product_description','stock','category','date_added','date_updated','image', 'image_url','image_thumbnail']
    search_fields = ['product_name','Product_description','category']
    list_filter = ['product_name','Product_description','category']

    def image_thumbnail(self,obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'No Image'
    image_thumbnail.short_description = 'image'


    