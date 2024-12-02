from django.contrib import admin
from .models import Item, OrderItem, Order

class Itemadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = [
        'title',
        'price',
        'discount_price',
    ]

admin.site.register(Item, Itemadmin)
admin.site.register(Order)
admin.site.register(OrderItem)