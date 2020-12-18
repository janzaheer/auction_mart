from django.contrib import admin

from .models import (
    Auction, Product, Category, Company, Attachment, CompanyUser)


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'status', 'published_date', 'start_time', 'end_time', 'start_date',
                    'end_date', )
    search_fields = ('title', 'company')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'auction', 'category', 'status', 'make', 'model', 'size', 'capacity', 'color', 'description',
                    'media', )
    search_fields = ('name', 'auction', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', )
    search_fields = ('name', 'status', )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'status', )
    search_fields = ('name', 'address', )


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('image', 'status', )


class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')
    search_fields = ('user__username',)
    raw_id_fields = ('user', 'company')


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)
