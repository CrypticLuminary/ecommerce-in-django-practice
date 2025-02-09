from django.contrib import admin
from .models import Buyer, Sales

@admin.register(Buyer)
class AdminBuyers(admin.ModelAdmin):
    def buyer_names(self, obj):
        return ', '.join([user.username for user in obj.buyer_name.all()])
    buyer_names.short_description = 'Buyer Names'
    
    list_display = ['buyer_names', 'buyes_on']
    search_fields = ['buyer_name__username']
    list_filter = ['buyes_on']

@admin.register(Sales)
class AdminSales(admin.ModelAdmin):
    def buyer_names(self, obj):
        return ', '.join([', '.join([user.username for user in buyer.buyer_name.all()]) 
                         for buyer in obj.buyer.all()])
    buyer_names.short_description = 'Buyer Names'
    
    list_display = ['product_name', 'buyer_names', 'quantity', 'date_of_purchase', 
                    'total_price', 'payment_method', 'payment_status']
    search_fields = ['product_name__product_name', 'buyer__buyer_name__username']
    list_filter = ['date_of_purchase', 'payment_method', 'payment_status']