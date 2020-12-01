from django.contrib import admin

from .models import (
    Auction, Product, Category, Company, Attachment, )


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'status', 'published_date', 'start_time', 'end_time', 'start_date',
                    'end_date', )
    search_fields = ('title', 'company')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'auction', 'category', 'status', 'make', 'model', 'size', 'capacity', 'color', 'description',
                    'media', )
    search_fields = ('name', 'auction', 'category')


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Product, ProductAdmin)
