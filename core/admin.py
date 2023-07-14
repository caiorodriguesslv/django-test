from django.contrib import admin
from .models import Client, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)

