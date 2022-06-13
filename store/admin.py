from django.contrib import admin
from .models import Store, Category

# Register your models here.
# admin.site.register(Store, Category)
@admin.register(Store)
class CustomCategory(admin.ModelAdmin):
    list_display = ('name', 'location', 'category')

@admin.register(Category)
class CustomCategory(admin.ModelAdmin):
    list_display = ('name',)
