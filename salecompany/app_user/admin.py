from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'birth_day', 'photo', 'dolznost', 'role', 'head', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'birth_day', 'photo', 'dolznost', 'role', 'head', 'is_staff', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'is_staff', 'is_active',)

admin.site.register(CustomUser, CustomUserAdmin)