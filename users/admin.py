from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('pk', 'email', 'first_name', 'last_name', 'phone', 'count_point', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    search_fields = ('email', 'first_name', 'last_name',)

admin.site.register(User, CustomUserAdmin)


