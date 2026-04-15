from django.contrib import admin
from .models import Product, Invoice, InvoiceItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'expiration_date', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at', 'expiration_date']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'created_at', 'get_total_amount', 'get_total_quantity']
    search_fields = ['invoice_number']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    def get_total_amount(self, obj):
        return f"{obj.get_total_amount():.2f}€"
    get_total_amount.short_description = 'Montant total'
    
    def get_total_quantity(self, obj):
        return obj.get_total_quantity()
    get_total_quantity.short_description = 'Nombre de produits'


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'product', 'quantity', 'unit_price', 'get_subtotal']
    search_fields = ['invoice__invoice_number', 'product__name']
    list_filter = ['invoice__created_at', 'product']
    
    def get_subtotal(self, obj):
        return f"{obj.get_subtotal():.2f}€"
    get_subtotal.short_description = 'Sous-total'
