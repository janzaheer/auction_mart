from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'mobile', 'full_name', 'address', 'created_at',)
    search_fields = ('user__username',)
    raw_id_fields = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
